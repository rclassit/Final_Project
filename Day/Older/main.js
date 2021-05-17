/**
* Template Name: Day - v4.1.0
* Template URL: https://bootstrapmade.com/day-multipurpose-html-template-for-free/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
f*/

function getSQLresults(){
    const url = 'http://127.0.0.1:5000//results/${tmp1}/${tmp2}/${tmp3}/${tmp4}/${tmp5}/${tmp6}';
    return fetch(url).then(response => response.json());

}

function grabparams(){
  //get inputs from dropdown in predictor section of html

  var overall = d3.select("#inputGroupSelect01").node().value;
  var aroma = d3.select("#inputGroupSelect02").node().value;
  var appearance = d3.select("#inputGroupSelect03").node().value;
  var palate = d3.select("#inputGroupSelect04").node().value;
  var taste = d3.select("#inputGroupSelect05").node().value;
  var ABV = d3.select("#inputGroupSelect06").node().value;

  //create array to input into model

  var input = [overall,aroma,appearance,palate,taste,ABV];
  console.log(input)
  res_array = getSQLresults(overall,aroma,appearance,palate,taste,ABV).then(response => {
    console.log(response);
    d3.select("#predictedBeer").text('Your perfect beer type is')
  })

}