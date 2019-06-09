$(document).ready(function()
{
  $("#header_form").submit(function(e) 
  {
    e.preventDefault();
    document.getElementById("mail_submit").style.display="none";
    document.getElementById("gif_mail").style.display="block";
    var site_name = $("#mail_header").val();
    var url = 'http://127.0.0.1:5000/send_header';
    document.getElementById("mail_info_row").style.visibility="hidden";
    document.getElementById("time_row").style.display="none";
    document.getElementById("check_row").style.display="none";
    document.getElementById("count_row").style.display="none";
    document.getElementById("url_row").style.display="none";
    
    $.ajax({
             type: "POST",
             url: url,
             dataType: 'json',
             contentType: 'application/json',
             data: JSON.stringify({header_ajax: site_name}),
             success: function(data)
             {
                if(data["header"].localeCompare("valid")==0)
                {
                    
                    document.getElementById("ip").innerHTL=data["IP"]
                    document.getElementById("hostname").innerHTML=data["Hostname"];
                    document.getElementById("organization").innerHTML=data["Organization"];
                    document.getElementById("amc_ch").innerHTML=data["time"];

                    protocol(data["SPF"],"SPF");
                    protocol(data["DKIM"],"DKIM");
                    protocol(data["DMARC"],"DMARC");

                    map(data["City"],data["Country"],data["Latitude"],data["Longitude"]);
                    links_call(site_name);   
                }
                else
                {
                    document.getElementById("mail_submit").style.display="block";
                    document.getElementById("gif_mail").style.display="none"; 
                    alert("Header not in correct format");
                }
             },
             error: function (jqXHR, exception) {
                 document.getElementById("mail_submit").style.display="block";
                 document.getElementById("gif_mail").style.display="none";   
                 alert("Internal Server Error"); 
             }
           });
  });
});



function protocol(value,type)
{
    if(value.localeCompare("none")==0)
    {
        value="fail"
    }
    document.getElementById(type).innerHTML = value;
    if(value.localeCompare("pass")==0)
    {
        document.getElementById(type).style.color = "green";
    }
    else if(value.localeCompare("fail")==0)
    {
        document.getElementById(type).style.color = "red";
    }
    else
    {
        document.getElementById(type).style.color = "yellow";
    }

}

function map(city,country,latitude,longitude)
{
    try
    {
        var latLang = [];
        var codecs = {};
        latLang.push([parseFloat(latitude),parseFloat(longitude)]);
        loc = ""
        if(city.localeCompare("n/a")==0)
        {
            if(country.localeCompare("n/a")==0)
            {
                loc = "n/a"
            }
            else
            {
                loc = country;
            }
        }
        else
        {
            loc = city+", "+country;
        }
        codecs[0]=loc;
        updatemap(latLang,codecs);
        document.getElementById("mail_info_row").style.visibility="visible";
        document.getElementById("time_row").style.display="block";
        document.getElementById("check_row").style.display="block";
        document.getElementById("count_row").style.display="none";
        document.getElementById("url_row").style.display="none";
    
    }
    catch(err){}
}



function updatemap(latLang, codecs)
{
  $("#map-2").vectorMap('get', 'mapObject').remove();
  $("#map-2").vectorMap({
        map : 'world_mill',
        zoomMin : '1',
        backgroundColor : '#888888',
        focusOn : {
          x : 0.5,
          y : 0.7,
          scale : 1
        },
        markers : latLang,
        markerStyle : {
          initial : {
            fill : '#ff4e50',
            stroke : '#ff4e50',
            "stroke-width" : 6,
            "stroke-opacity" : 0.3,
          }
        },
        zoomMax : 1,
        regionStyle : {
          initial : {
            fill : '#e9e9e9',
            "fill-opacity" : 1,
            stroke : 'none',
            "stroke-width" : 0,
            "stroke-opacity" : 1
          },
          hover : {
            "fill-opacity" : 0.8
          },
          selected : {
            fill : 'yellow'
          },
          selectedHover : {}
        },
        labels: 
          {
              markers: 
              {
                  render: function(code)
                  {
                    return codecs[code];
                  },
                    offsets: function(code){
                      return [0,0];
                    }
                
              }
          }
        });
}

function links_call(header)
{
    var url = 'http://127.0.0.1:5000/mail_links';
    $.ajax({
     type: "POST",
     url: url,
     dataType: 'json',
     contentType: 'application/json',
     data: JSON.stringify({header_ajax: header}),
     success: function(data)
     {
        document.getElementById("mail_submit").style.display="block";
        document.getElementById("gif_mail").style.display="none"; 
        links_update(data["links"],data["predictions"]);
     },
     error: function (jqXHR, exception) {
         document.getElementById("mail_submit").style.display="block";
         document.getElementById("gif_mail").style.display="none"; 
         links_update([],[]);
     }
   });
}


function links_update(links,predictions)
{
    document.getElementById("mail_info_row").style.visibility="visible";
    document.getElementById("time_row").style.display="block";
    document.getElementById("check_row").style.display="none";
    document.getElementById("count_row").style.display="block";
    document.getElementById("url_row").style.display="block";
    var url_row = document.getElementById("url_row");
    while (url_row.firstChild) {
           url_row.removeChild(url_row.firstChild);
        }

    document.getElementById("dmc").innerHTML=links.length;
    for(i=0;i<links.length;i++)
    {
        var a = document.createElement('a');
        var linkText = document.createTextNode(links[i]);
        a.appendChild(linkText);
        a.href=links[i];
        if(predictions[i].localeCompare("1")==0)
        {
            a.className="url_good";
        }

        if(predictions[i].localeCompare("-1")==0)
        {
            a.className="url_bad";
        }

        var url_row = document.getElementById("url_row");

        url_row.appendChild(a);
        url_row.appendChild(document.createElement("BR"));
        
    }
}