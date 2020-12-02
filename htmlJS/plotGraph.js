Plotly.d3.csv("C:/Users/afarruggia/Documents/0 - Personal/ts/htmlJS/EURUSD_Candlestick_1_Hour_BID_18.09.2015-15.09.2018.csv", function(err, rows){

function unpack(rows, key) {
  return rows.map(function(row) {
    return row[key];
  });
}

var trace = {
  x: unpack(rows, 'Gmt time'),
  close: unpack(rows, 'Close'),
  high: unpack(rows, 'High'),
  low: unpack(rows, 'Low'),
  open: unpack(rows, 'Open'),

  // cutomise colors
  increasing: {line: {color: 'green'}},
  decreasing: {line: {color: 'red'}},

  type: 'candlestick',
  xaxis: 'x',
  yaxis: 'y'
};

var trace2 = {
  
  x: ['2017-01-04', '2017-01-05', '2017-01-06', '2017-01-09', '2017-01-10'], 
  
  close: [116.019997, 116.610001, 117.910004, 118.989998, 119.110001], 
  
  decreasing: {line: {color: 'red'}}, 
  
  high: [116.510002, 116.860001, 118.160004, 119.43, 119.379997], 
  
  increasing: {line: {color: 'green'}}, 
  
  line: {color: 'rgba(31,119,180,1)'}, 
  
  low: [115.75, 115.809998, 116.470001, 117.940002, 118.300003], 
  
  open: [115.849998, 115.919998, 116.779999, 117.949997, 118.769997], 
  
  type: 'candlestick', 
  xaxis: 'x', 
  yaxis: 'y'
};

var data = [trace];

var layout = {
  dragmode: 'zoom',
  showlegend: false,
  xaxis: {
    rangeslider: {
     visible: false
   }
  }
};

Plotly.plot('tester', data, layout);
});