import { Component, OnInit } from '@angular/core';

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
  isWaiting: boolean = false
  pages: string[] = []
  activePage:number = 1

  searchTerm(term: string, page: string){
    if(term === '')
      return
    this.isWaiting = true;
    this.searchService.getSearchSentence(term, page)
      .subscribe((result:any) => {
        let from = 1;
        let end = parseInt(result.total_results) / 10

        this.activePage = result.page
        this.pages = []
        for(let i = from ; i <= end ; i++)
          this.pages.push(i.toString())

        this.searchResult = {
         "search_time" : result.search_time,
         "total_results": result.total_results 
        }
        this.sentences = result.sentences
        this.isWaiting = false
      })
    console.log(this.searchResult)
  }
}