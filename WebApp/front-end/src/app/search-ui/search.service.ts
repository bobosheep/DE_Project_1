import { Injectable } from '@angular/core'
import { HttpClient, HttpParams } from '@angular/common/http'
import { HttpHeaders } from '@angular/common/http'
import { sentence } from './sentence'
import { Observable } from 'rxjs'

const httpOptions = {
    header: new HttpHeaders({
        "Content-Type":  "application/json"
    })
}

@Injectable()
export class myHttpService {
    constructor(private http: HttpClient){}


    getSearchSentence(term: string, page: string): Observable< any >{
        const options = term ?
        { params: new HttpParams().set('term', term).append('page', page) } : {};
        return this.http.get<any>(`http://localhost:5000/search`, options)
    }
}