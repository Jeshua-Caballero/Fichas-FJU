const barras = document.querySelector('.bars');
barras.addEventListener('click', (e)=> {
    e.preventDefault();
    modNav();
    modSidebar();
    modMainContent();
});
function modNav () {
    const mainNav = document.querySelector('.main-nav ');
    const styleNav = getComputedStyle(mainNav);
    if (parseInt(styleNav.marginLeft, 10) === 230) {
        mainNav.style.marginLeft = "50px"
    } else {
        mainNav.style.marginLeft = "230px"
    };
}

function modSidebar () {
    const logoSmall = document.querySelector('.logo-small');
    const logoLarge = document.querySelector('.logo-large');
    const mainSidebar = document.querySelector('.main-sidebar');

    const itemAside = document.querySelectorAll('.list-aside__item');

    if (parseInt(getComputedStyle(mainSidebar).width, 10) === 230) {
        mainSidebar.style.width = "50px"
        logoSmall.hidden=false;
        logoLarge.hidden=true;
    } else {
        mainSidebar.style.width = "230px"
        logoLarge.hidden=false;
        logoSmall.hidden=true;
    }

    const styleSidebar = getComputedStyle(mainSidebar);
    for (const item of itemAside) {
        const enlaceAside = item.firstElementChild
        const span = enlaceAside.lastElementChild
        if (parseInt(styleSidebar.width, 10) === 230) {
            span.hidden = false;
        } else {
            span.hidden = true;
        };
    };
}

function modMainContent () {
    const modMainContent = document.querySelector('.main-content');
    const styleMainContent = getComputedStyle(modMainContent);
    if (parseInt(styleMainContent.marginLeft, 10) === 230) {
        modMainContent.style.marginLeft = "50px"
    } else {
        modMainContent.style.marginLeft = "230px"
    }
}

const canvas = document.getElementById('my-chart');
const tribu = ['Ruben','Simeón','Leví','Judá','Isacar','Zabulón','Dan','Neftalí','Gad','Aser','José','Benjamín'];
const count = [14,12,8,24,10,19,28,30,11,7,15,32];

const myChart = new Chart(canvas, {
    type : 'doughnut',
    data : {
        labels : tribu,
        datasets : [{
            label : 'Cantidad',
            data : count,
            backgroundColor : [
                '#E0115F',
                '#50C878',
                '#E0FFFF',
                '#0F52BA',
                '#40E0D0',
                '#6A0DAD',
                '#1D3557',
                '#B0B0B0',
                '#D2B48C',
                '#556B2F',
                '#000000',
                '#9966CC'
            ],
            borderColor : 'black',
            borderWidth : 1.5
        }]
    },
    options : {
        plugins : {
            legend: { 
                position: 'right',
                labels: {
                    color: 'black', // Cambia el color de los labels
                    font: {
                        size: 15, // Cambia el tamaño de la fuente
                        weight: '100' // Cambia el grosor de la fuente
                    },
                    boxWidth: 20, // Ancho de la caja de color junto al label
                    boxHeight: 10, // Altura de la caja de color
                    padding: 15, // Espacio entre cada item de la leyenda
                    usePointStyle: true, // Cambia el estilo de la caja de color a un punto
                    pointStyle: 'rectRounded', // Estilo del punto (circle, rect, rectRounded, etc.)
                }
            }
        }
    }
}); 