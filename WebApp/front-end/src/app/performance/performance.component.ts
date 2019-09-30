import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-performance',
  templateUrl: './performance.component.html',
  styleUrls: ['./performance.component.css']
})
export class PerformanceComponent implements OnInit {


  performances: any[] = [{
    title : 'Proj.1 斷句與搜尋 Breaking Sentences and Searching',
    subtitle : 'Performance', 
    panels : [
      {
        title: 'Parse articles',
        subtitle : 'from 1.88 GB data',
        contents : ['Total articles: 829,787','Time cost: 18.7664 s',
                    'Average time cost per article: 0.0226 ms'
                  ]
      },
      {
        title: 'Split',
        subtitle : 'about 829787 articles',
        contents : ['Total sentences: 15,148,116',
                    'Split time cost: 129.065 s',
                    'Average split time cost per sentence: 0.00852 ms'
                  ]
      },
      {
        title: 'Sort',
        subtitle : '15,148,116 sentences',
        contents : ['Total sentences: 15,148,116',
                   'Sort time cost: 4.719 s',
                  ]  
        
      },
    ]
  }]


  constructor() { }

  ngOnInit() {
  }

}
