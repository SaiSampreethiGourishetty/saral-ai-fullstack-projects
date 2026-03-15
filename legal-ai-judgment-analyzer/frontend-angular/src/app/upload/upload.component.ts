import { Component } from '@angular/core';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html'
})
export class UploadComponent {

  file:any
  result:any

  constructor(private api:ApiService){}

  onFileSelect(event:any){
    this.file = event.target.files[0]
  }

 upload(){

  this.api.analyze(this.file)
  .subscribe((res:any)=>{
    this.result = res
  })

}

}
