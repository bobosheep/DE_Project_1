import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-project-description',
  templateUrl: './project-description.component.html',
  styleUrls: ['./project-description.component.css']
})
export class ProjectDescriptionComponent implements OnInit {

  projects: any[] = [{
    title : 'Proj.1 斷句與搜尋',
    subtitle : 'Breaking Sentences and Searching', 
    content : '根據提供之新聞資料（約1.9 GB）將所有文章內容做斷句，\
               並將其排序、計算句子重複次數，最後以網頁型式呈現，並提供簡單搜尋功能。',
    links: [{url:'/search', text:'Go Search'}, {url:'/performance', text:'Performance'},
            {url:'/all-sentence', text:'Sentences'}] 
  }]

  constructor() { }

  ngOnInit() {
  }

}
