import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'covidGraphs';

  fechaActual: any;
  fechas: any[]=[];
  imagenes: any[]=[];

  ngOnInit(): void {
    for(let i = 2; i < 10; i++){
      this.fechas[i-2] = i+"-"+12;
    }
    this.primeraFecha();
  }

  primeraFecha(){
    this.fechaActual = this.fechas[0];
    this.imagenes[0] = "https://proyecto-big-data-jsj.s3.amazonaws.com/graficas/0"+this.fechaActual+"/muertes_departamento.png";
    this.imagenes[1] = "https://proyecto-big-data-jsj.s3.amazonaws.com/graficas/0"+this.fechaActual+"/muertes_edad.png";
    this.imagenes[2] = "https://proyecto-big-data-jsj.s3.amazonaws.com/graficas/0"+this.fechaActual+"/muertes_genero.png";
    this.imagenes[3] = "https://proyecto-big-data-jsj.s3.amazonaws.com/graficas/0"+this.fechaActual+"/muertes_extrangeros.png";
  }

  calcular(i:number){
    this.fechaActual = this.fechas[i];
    this.imagenes[0] = "https://proyecto-big-data-jsj.s3.amazonaws.com/graficas/0"+this.fechaActual+"/muertes_departamento.png";
    this.imagenes[1] = "https://proyecto-big-data-jsj.s3.amazonaws.com/graficas/0"+this.fechaActual+"/muertes_edad.png";
    this.imagenes[2] = "https://proyecto-big-data-jsj.s3.amazonaws.com/graficas/0"+this.fechaActual+"/muertes_genero.png";
    this.imagenes[3] = "https://proyecto-big-data-jsj.s3.amazonaws.com/graficas/0"+this.fechaActual+"/muertes_extrangeros.png";
  }
}
