// NEED TO JSONIFY SPIRIT_TOTAL.CSV IN ORDER TO MAKE BUBBLE PLOT
// FLASK FEEDS JSON DATA: 
// 1. JAVASCRIPT CALLS TO FLASK FROM APP.PY
// 2. FLASK CALLS/QUERIES THE DATABASE 
// 3. RETURNS IN JSON FORMAT
// DON'T FORGET TO ADD PLOTLY CODE TO THE INDEX.HTML





  url ="http://localhost:5000/api/v1.0/spirit_totals"
  d3.json(url, function(data) { 
    console.log(data);

    var s_array = []
    var t_array =[]

    for (var s = 0; s < data.length; s++) {
      var s_dict = data[s];
      
      // push each spirit  and total value into own array
        s_array.push(s_dict["spirit"]);
        t_array.push(s_dict["total"])
      }
      
    // var spirit = s_array;
    // var totals = t_array;
    
      
    var trace1 = {
      values: t_array,
      labels: s_array,
      type: "pie"
      
    };

    var data = [trace1];

    var layout = {
      
      title: "Cocktail Spirit Totals",
      height: 400,
      width: 550,
      plot_bgcolor:'rgba(0,0,0,0)',
      paper_bgcolor:'rgba(0,0,0,0)',
      font: {
        color: 'ffffff'
      }
      };
    
    // var layout = {
    //   title: "Cocktail Spirit Totals",
    //   xaxis: { 
    //     range: [0,100],
    //     type: "number"
    // },
    //   yaxis: {
    //     autorange: true,
    //     type: "linear"
    // }
  Plotly.newPlot("plot", data, layout);
  });
 
  
 

