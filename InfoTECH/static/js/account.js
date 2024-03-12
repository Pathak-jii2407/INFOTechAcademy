function changeProfileImage() {
    var image = document.getElementById('profileImage');
    var images = [
      'https://source.unsplash.com/300x200/?nature',
      'https://source.unsplash.com/300x200/?technology',
      'https://source.unsplash.com/300x200/?architecture',
      'https://source.unsplash.com/300x200/?food',
      'https://source.unsplash.com/300x200/?travel'
    ];
    var randomIndex = Math.floor(Math.random() * images.length);
    image.src = images[randomIndex];
}

document.addEventListener("DOMContentLoaded", function() {
    var canvas = document.getElementById("pie-chart");
    var ctx = canvas.getContext("2d");
  
    var data = {
      labels: ["Python", "Java", "JavaScript", "HTML/CSS"],
      datasets: [{
        data: [32, 66, 89, 121],
        backgroundColor: [
          'rgba(255, 99, 132, 0.6)',
          'rgba(54, 162, 235, 0.6)',
          'rgba(255, 206, 86, 0.6)',
          'rgba(75, 192, 192, 0.6)'
        ]
      }]
    };
  
    var options = {
      responsive: true,
      maintainAspectRatio: false,
      legend: {
        position: 'right'
      }
    };
  
    var pieChart = new Chart(ctx, {
      type: 'pie',
      data: data,
      options: options
    });
});

