$(document).ready(function()
{
  $("#ajax_form").submit(function(e) 
  {
    e.preventDefault();
    document.getElementById("submit").style.display="none";
    document.getElementById("gif").style.display="block";
    var site_name = $("#url_ajax").val();
    var url = 'http://127.0.0.1:5000/send_result';
    document.getElementById("result_row").style.display="none";
    document.getElementById("server_row").style.display="none";
    document.getElementById("features_row").style.display="none";

    $.ajax({
             type: "POST",
             url: url,
             dataType: 'json',
             contentType: 'application/json',
             data: JSON.stringify({url_ajax: site_name}),
             success: function(data)
             {
                 document.getElementById("submit").style.display="block";
                 document.getElementById("gif").style.display="none";

                 document.getElementById("cover_image").src='http://127.0.0.1:5000/send_file?url_ajax='+site_name;
                 var domain = site_name.split("//").slice(-1).pop().split('/')[0].split("www.").slice(-1).pop();
                 document.getElementById("domain_name").innerHTML="Domain Name: "+domain;
                 
                 re_value=prediction(data["prediction"]);
                 if(re_value==0)
                 {
                   web_traffic(data["web_traffic"]);
                   google_indexed(data["google_index"]);
                   backlinks(data["links_pointing"]);
                   age(data["age_of_domain"]);
                   reg_length(data["domain_registration"]);
                   url_length(data["url_length"]);
                   url_short(data["url_short"]);
                   at_symbol(data["having_at_symbol"]);
                   prefix(data["prefix_suffix"]);
                   https(data["https_token"]);
                   request_url(data["request_url"]);
                   anchor(data["url_of_anchor"]);
                   meta_links(data["Links_in_tags"]);
                   ip(data["url_having_ip"]);
                   doubleslash(data["doubleSlash"]);
                   redirect(data["redirect"]);
                   mail(data["email_submit"]);
                   iframe(data["iframe"]);
                   ssl(data["SSLfinal_State"]);
                   subdomain(data["sub_domain"]);
                   location_ajax(site_name);
                }
             },
             error: function (jqXHR, exception) {
                 alert("Internal Server Error");
                 document.getElementById("submit").style.display="block";
                 document.getElementById("gif").style.display="none";   
             }
           });
  });
});


function prediction(predict)
{
  if(parseInt(predict)==-1)
  {
    document.getElementById("result").innerHTML = "Phishing" ;
    document.getElementById("result").style.color = "red";
    return 0;
  }
  else if(parseInt(predict)==1)
  {
    document.getElementById("result").innerHTML = "Legitimate";
    document.getElementById("result").style.color = "green";
    return 0;
  }
  else if(predict=="Invalid")
  {
    alert("Please check URL format");
    return 1;
  }

  else if(predict=="Error")
  {
    alert("Internal Server Error")
    return 2;
  }
}



function web_traffic(value)
{
  //if(parseInt(value)<=10000 && parseInt(value)>=0)
  //{
    //document.getElementById("result").innerHTML = "Legitimate";
    //document.getElementById("result").style.color = "green";
  //}
  if(parseInt(value)==-1)
  {
    document.getElementById("web_traffic").innerHTML = +"No Rank<br>(Phishing)";
    document.getElementById("web_traffic").style.color = "red";
  }
  else if(parseInt(value)<=100000)
  {
    document.getElementById("web_traffic").innerHTML = value+"<br>(Legitimate)" ;
    document.getElementById("web_traffic").style.color = "green";
  }
  else if(parseInt(value)>100000)
  {
    document.getElementById("web_traffic").innerHTML = value+"<br>(Suspicious)";
    document.getElementById("web_traffic").style.color = "yellow";
  }
 
}




function google_indexed(value)
{
  
  if(parseInt(value)==1)
  {
    document.getElementById("google_indexed").innerHTML = "Yes<br>(Legitimate)" ;
    document.getElementById("google_indexed").style.color = "green";
  }
  else if(parseInt(value)==-1)
  {
    document.getElementById("google_indexed").innerHTML = "No<br>(Phishing)";
    document.getElementById("google_indexed").style.color = "red";
  }
 
}


function backlinks(value)
{
  if(Number.isInteger(value)==true)
  {
    if(res==0)
    {
      document.getElementById("backlinks").innerHTML = res+"<br>(Phishing)" ;
      document.getElementById("backlinks").style.color = "red";
    }
    else if(res<=2)
    {
      document.getElementById("backlinks").innerHTML = res+"<br>(Suspicious)";
      document.getElementById("backlinks").style.color = "yellow";
    }
    else
    {
      document.getElementById("backlinks").innerHTML = res+"<br>(Legitimate)";
      document.getElementById("backlinks").style.color = "green";
    }
  }
  else
  {
    document.getElementById("backlinks").innerHTML = value+"<br>(Legitimate)" ;
    document.getElementById("backlinks").style.color = "green";
  }
 
}

function age(value)
{
  
  if(parseInt(value)>=180)
  {
    document.getElementById("age").innerHTML = value+" days<br>(Legitimate)" ;
    document.getElementById("age").style.color = "green";
  }
  else
  {
    document.getElementById("age").innerHTML = value+" days<br>(Phishing)";
    document.getElementById("age").style.color = "red";
  }
 
}

function reg_length(value)
{
  
  if(parseInt(value)>=365)
  {
    document.getElementById("reg_length").innerHTML = value+" days<br>(Legitimate)" ;
    document.getElementById("reg_length").style.color = "green";
  }
  else
  {
    document.getElementById("reg_length").innerHTML = value+" days<br>(Phishing)";
    document.getElementById("reg_length").style.color = "red";
  }
 
}


function url_length(value)
{
  
  if(parseInt(value)<54)
  {
    document.getElementById("length").innerHTML = value+" <br>(Legitimate)" ;
    document.getElementById("length").style.color = "green";
  }

  else if(parseInt(value)>=54 && parseInt(value)<=75)
  {
    document.getElementById("length").innerHTML = value+" <br>(Suspicious)" ;
    document.getElementById("length").style.color = "yellow";
  }
  else
  {
    document.getElementById("length").innerHTML = value+" <br>(Phishing)";
    document.getElementById("length").style.color = "red";
  }
 
}

function url_short(value)
{
  
  if(parseInt(value)==1)
  {
    document.getElementById("url_short").innerHTML = "No <br>(Legitimate)" ;
    document.getElementById("url_short").style.color = "green";
  }

  else if(parseInt(value)==-1)
  {
    document.getElementById("url_short").innerHTML = "Yes <br>(Phishing)" ;
    document.getElementById("url_short").style.color = "red";
  }
 
}

function at_symbol(value)
{
  
  if(parseInt(value)==1)
  {
    document.getElementById("at_symbol").innerHTML = "No <br>(Legitimate)" ;
    document.getElementById("at_symbol").style.color = "green";
  }

  else if(parseInt(value)==-1)
  {
    document.getElementById("at_symbol").innerHTML = "Yes <br>(Phishing)" ;
    document.getElementById("at_symbol").style.color = "red";
  }
 
}


function prefix(value)
{
  
  if(parseInt(value)==1)
  {
    document.getElementById("prefix").innerHTML = "No <br>(Legitimate)" ;
    document.getElementById("prefix").style.color = "green";
  }

  else if(parseInt(value)==-1)
  {
    document.getElementById("prefix").innerHTML = "Yes <br>(Phishing)" ;
    document.getElementById("prefix").style.color = "red";
  }
 
}

function https(value)
{
  
  if(parseInt(value)==1)
  {
    document.getElementById("https").innerHTML = "No <br>(Legitimate)" ;
    document.getElementById("https").style.color = "green";
  }

  else if(parseInt(value)==-1)
  {
    document.getElementById("https").innerHTML = "Yes <br>(Phishing)" ;
    document.getElementById("https").style.color = "red";
  }
 
}

function request_url(value)
{
  
  if(parseFloat(value)<0.22 && parseFloat(value)>=0)
  {
    document.getElementById("request_url").innerHTML = (Math.round(value*100))+"% <br>(Legitimate)" ;
    document.getElementById("request_url").style.color = "green";
  }

  else if(parseFloat(value)>=0.22 && parseFloat(value)<=0.61)
  {
    document.getElementById("request_url").innerHTML = (Math.round(value*100))+"% <br>(Suspicious)" ;
    document.getElementById("request_url").style.color = "yellow";
  }


  else if(parseFloat(value)>0.61)
  {
    document.getElementById("request_url").innerHTML = (Math.round(value*100))+"% <br>(Phishing)" ;
    document.getElementById("request_url").style.color = "red";
  }
  else if(parseFloat(value)==-1)
  {
    document.getElementById("request_url").innerHTML = "Unknown <br>(Suspicious)" ;
    document.getElementById("request_url").style.color = "yellow";
  }
 
}


function anchor(value)
{
  
  if(parseFloat(value)<0.31 && parseFloat(value)>=0)
  {
    document.getElementById("anchor").innerHTML = (Math.round(value*100))+"% <br>(Legitimate)" ;
    document.getElementById("anchor").style.color = "green";
  }

  else if(parseFloat(value)>=0.31 && parseFloat(value)<=0.67)
  {
    document.getElementById("anchor").innerHTML = (Math.round(value*100))+"% <br>(Suspicious)" ;
    document.getElementById("anchor").style.color = "yellow";
  }


  else if(parseFloat(value)>0.67)
  {
    document.getElementById("anchor").innerHTML = (Math.round(value*100))+"% <br>(Phishing)" ;
    document.getElementById("anchor").style.color = "red";
  }
  else if(parseFloat(value)==-1)
  {
    document.getElementById("anchor").innerHTML = "Unknown <br>(Suspicious)" ;
    document.getElementById("anchor").style.color = "yellow";
  }
 
}

function meta_links(value)
{
  
  if(parseFloat(value)<0.17 && parseFloat(value)>=0)
  {
    document.getElementById("meta_links").innerHTML = (Math.round(value*100))+"% <br>(Legitimate)" ;
    document.getElementById("meta_links").style.color = "green";
  }

  else if(parseFloat(value)>=0.17 && parseFloat(value)<=0.81)
  {
    document.getElementById("meta_links").innerHTML = (Math.round(value*100))+"% <br>(Suspicious)" ;
    document.getElementById("meta_links").style.color = "yellow";
  }


  else if(parseFloat(value)>0.81)
  {
    document.getElementById("meta_links").innerHTML = (Math.round(value*100))+"% <br>(Phishing)" ;
    document.getElementById("meta_links").style.color = "red";
  }
  else if(parseFloat(value)==-1)
  {
    document.getElementById("meta_links").innerHTML = "Unknown <br>(Suspicious)" ;
    document.getElementById("meta_links").style.color = "yellow";
  }
 
}


function ip(value)
{
  
  if(parseInt(value)==1)
  {
    document.getElementById("ip").innerHTML = "No <br>(Legitimate)" ;
    document.getElementById("ip").style.color = "green";
  }

  else if(parseInt(value)==-1)
  {
    document.getElementById("ip").innerHTML = "Yes <br>(Phishing)" ;
    document.getElementById("ip").style.color = "red";
  }
 
}

function doubleslash(value)
{
  
  if(parseInt(value)==1)
  {
    document.getElementById("doubleslash").innerHTML = "No <br>(Legitimate)" ;
    document.getElementById("doubleslash").style.color = "green";
  }

  else if(parseInt(value)==-1)
  {
    document.getElementById("doubleslash").innerHTML = "Yes <br>(Phishing)" ;
    document.getElementById("doubleslash").style.color = "red";
  }
 
}


function redirect(value)
{
  
  if(parseInt(value)==1)
  {
    document.getElementById("redirect").innerHTML = "Less than 4<br>(Legitimate)" ;
    document.getElementById("redirect").style.color = "green";
  }

  else if(parseInt(value)==0)
  {
    document.getElementById("redirect").innerHTML = "More than 4<br>(Phishing)" ;
    document.getElementById("redirect").style.color = "red";
  }
 
}

function mail(value)
{
  
  if(parseInt(value)==1)
  {
    document.getElementById("mail").innerHTML = "No<br>(Legitimate)" ;
    document.getElementById("mail").style.color = "green";
  }

  else if(parseInt(value)==-1)
  {
    document.getElementById("mail").innerHTML = "Yes<br>(Phishing)" ;
    document.getElementById("mail").style.color = "red";
  }
 
}

function iframe(value)
{
  
  if(parseInt(value)==1)
  {
    document.getElementById("iframe").innerHTML = "No Iframe<br>(Legitimate)" ;
    document.getElementById("iframe").style.color = "green";
  }

  else if(parseInt(value)==-1)
  {
    document.getElementById("iframe").innerHTML = "Iframe Found<br>(Phishing)" ;
    document.getElementById("iframe").style.color = "red";
  }
 
}

function ssl(value)
{
  
  if(parseInt(value)==1)
  {
    document.getElementById("ssl").innerHTML = "Trusted Certificate<br>(Legitimate)" ;
    document.getElementById("ssl").style.color = "green";
  }

  else if(parseInt(value)==-1)
  {
    document.getElementById("ssl").innerHTML = "No Certificate Found<br>(Phishing)" ;
    document.getElementById("ssl").style.color = "red";
  }

  else if(parseInt(value)==0)
  {
    document.getElementById("ssl").innerHTML = "Untrusted Certificate<br>(Suspicious)" ;
    document.getElementById("ssl").style.color = "yellow";
  }
 
}


function subdomain(value)
{
  
  if(parseInt(value)==1)
  {
    document.getElementById("subdomain").innerHTML = "No<br>(Legitimate)" ;
    document.getElementById("subdomain").style.color = "green";
  }

  else if(parseInt(value)==0)
  {
    document.getElementById("subdomain").innerHTML = "1 SubDomain<br>(Suspicious)" ;
    document.getElementById("subdomain").style.color = "yellow";
  }

  else if(parseInt(value)==-1)
  {
    document.getElementById("subdomain").innerHTML = "More than 1<br>(Phishing)" ;
    document.getElementById("subdomain").style.color = "red";
  }
 
}


function location_ajax(site_name)
{
  var url = 'http://127.0.0.1:5000/send_location?url_ajax='+site_name;
  $.ajax({
    type: "GET",
    url: url,
    success: function(data)
    {
      latitudes = data["latitude"];
      if(latitudes!="null")
      {
        document.getElementById("result_row").style.display="block";
        document.getElementById("server_row").style.display="block";
        document.getElementById("features_row").style.display="block";

        var latLang = [];
        var codecs = {};
        for (i=0; i<latitudes.length; i++)
        {
           latLang.push([parseFloat(data["latitude"][i]),parseFloat(data["longitude"][i])]);
           //latLang.push(parseFloat(data["latitude"][i]),parseFloat(data["longitude"][i]));
           loc = ""
           if(data["city"]=="unknown")
           {
            if(data["country"]=="unknown")
            {
              loc = "unknown"
            }
            else
            {
              loc = data["country"];
            }
           }
           else
           {
            loc = data["city"]+", "+data["country"];
           }
           codecs[i]=loc;
         }
         updatemap(latLang,codecs);
      }
      else
      {
        alert("URL Not reachable");
      }
    }
  });
}


function updatemap(latLang, codecs)
{
  //alert(latLang)
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

