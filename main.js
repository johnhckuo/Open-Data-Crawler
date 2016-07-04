var fs = require("fs");
var request = require("request");
var $ = require("jquery");
var result = [];
var j = 0;


function ajax(url){
    request({
        url: url,
        json: true
    }, function (error, response, body) {
     
        if (!error && response.statusCode === 200) {
        	for (var i  = 0 ; i < body.data.length; i ++){
        		//console.log(body.data[i].message.toString('big5'))
        		var str = body.data[i].message
        		
        		if (str != undefined){
        			var n = str.indexOf("正義曙光");
        			var m = str.indexOf("超人");
        		}
        		console.log(n)
        		if (n != -1 || m != -1){
        			if (str != undefined){
        				result = result.concat(body.data[i]);
        				fs.writeFile("et.json", JSON.stringify(result),function(){
        					console.log("DONE !");
        				});
        			}
        		}
        	}
        	url = body.paging.next;
        	if (url && j < 1000){
        		ajax(url);
          		j++;
        	}
//            result = result.concat(body.data);
            
//            j++;
//            fs.writeFile("result.json", JSON.stringify(result),function(){
//                console.log("DONE !");
//            });
//            if (url && j < 600){
//                ajax(url);
//                j++;
//            }
        }
    });
     
}
 
var url = "https://graph.facebook.com/v2.6/242305665805605/posts?fields=likes.limit(0).summary(true)%2Ccomments.limit(0).summary(true)%2Cmessage%2Ccreated_time&limit=25&__paging_token=enc_AdCgO95mmXys1vuhL4E59yHZA4WPiO6YA6jxZBNgD9F7bU7VcgVki2UHyYCTeEMO90BNlxAsWl3ZBA0cdmWyfFLuY9opcZA7A8mlKTB2XMC2n4TcJgZDZD&since=1462916400&__previous=1&access_token=EAACEdEose0cBAJmzqtc6bBQMT0ZAlZB3FCBRNYBIZAc1YnJXv2O5D8k31rbObltaUVSKZB1doYwFQlUXi73rkNr2MPlWN4cEk57qCau6lzdm252xZChndvNGZBfrKFWQXG3xrQUeXGIZCkEZARwYqNsS6OWZCVvV90WijKlyz03h0CwZDZD";
ajax(url);
 
 
 
 
//fs.readFile("john.json", "UTF-8", function(err, data){
//  console.log(data);
//});