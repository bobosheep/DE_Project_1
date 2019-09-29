import { Component, OnInit } from '@angular/core';
//import sentence_data from '../../../sentences.json'
import { HttpClient } from '@angular/common/http';

import { myHttpService } from './search.service';

@Component({
  selector: 'search-ui',
  templateUrl: './search-ui.component.html',
  styleUrls: ['./search-ui.component.css']
})
export class SearchUiComponent implements OnInit {

  constructor(private searchService: myHttpService) { }

  ngOnInit() {
  }
  config: any = {
    "url" : 'localhost:5000'
  }
  searchResult : any = {}
  sentences: any[] = [] 

  searchTerm(term: string){
    if(term === '')
      return
    this.searchService.getSearchSentence(term)
      .subscribe((result:any) => {
        this.searchResult = {
         "search_time" : result.search_time,
         "total_results": result.total_results 
        }
        this.sentences = result.sentences
      })
    console.log(this.searchResult)
  }
}