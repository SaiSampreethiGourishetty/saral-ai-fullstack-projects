import { Injectable } from '@angular/core'
import { HttpClient } from '@angular/common/http'

@Injectable({
  providedIn:'root'
})
export class ApiService{

  constructor(private http:HttpClient){}

  analyze(file:File){

    const formData = new FormData()
    formData.append("file",file)

    return this.http.post(
      "http://localhost:8080/api/legal/analyze",
      formData
    )

  }

}
