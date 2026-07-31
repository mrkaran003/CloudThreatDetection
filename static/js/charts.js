document.addEventListener("DOMContentLoaded", function () {

    const chartCanvas = document.getElementById(
        "threatChart"
    );

    if (!chartCanvas) {

        return;

    }

    new Chart(chartCanvas, {

        type: "doughnut",

        data: {

            labels: [

                "Critical Threats",
                "High Risk",
                "Medium Risk",
                "Low Risk",
                "Safe Logs"

            ],

            datasets: [

                {

                    data: [

                        window.criticalRisk || 0,

                        window.highRisk || 0,

                        window.mediumRisk || 0,

                        window.lowRisk || 0,

                        window.safeLogs || 0

                    ],

                    backgroundColor: [

                        "#dc2626",

                        "#f97316",

                        "#eab308",

                        "#22c55e",

                        "#3b82f6"

                    ],

                    borderColor: "#0d1117",

                    borderWidth: 3,

                    hoverOffset: 20

                }

            ]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            cutout: "65%",

            plugins: {

                legend: {

                    position: "bottom",

                    labels: {

                        color: "white",

                        font: {

                            size: 14,

                            weight: "bold"

                        },

                        padding: 20

                    }

                },

                title: {

                    display: true,

                    text: "Cloud Threat Analytics",

                    color: "white",

                    font: {

                        size: 20

                    }

                }

            },

            animation: {

                animateRotate: true,

                animateScale: true

            }

        }

    });

});