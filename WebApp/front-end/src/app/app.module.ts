import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { CdkTableModule } from '@angular/cdk/table';
import { CdkTreeModule } from '@angular/cdk/tree';
import { RouterModule, Routes } from '@angular/router';
import { APP_BASE_HREF } from '@angular/common';
import {
  MatAutocompleteModule,
  MatBadgeModule,
  MatBottomSheetModule,
  MatButtonModule,
  MatButtonToggleModule,
  MatCardModule,
  MatCheckboxModule,
  MatChipsModule,
  MatDatepickerModule,
  MatDialogModule,
  MatDividerModule,
  MatExpansionModule,
  MatGridListModule,
  MatIconModule,
  MatInputModule,
  MatListModule,
  MatMenuModule,
  MatNativeDateModule,
  MatPaginatorModule,
  MatProgressBarModule,
  MatProgressSpinnerModule,
  MatRadioModule,
  MatRippleModule,
  MatSelectModule,
  MatSidenavModule,
  MatSliderModule,
  MatSlideToggleModule,
  MatSnackBarModule,
  MatSortModule,
  MatStepperModule,
  MatTableModule,
  MatTabsModule,
  MatToolbarModule,
  MatTooltipModule,
  MatTreeModule,
} from '@angular/material';

import { HomeComponent } from './home/home.component';
import { SearchUiComponent } from './search-ui/search-ui.component';
import { myHttpService } from './search-ui/search.service';
import { ProjectDescriptionComponent } from './project-description/project-description.component';
import { AllSentenceComponent } from './all-sentence/all-sentence.component';
import { PerformanceComponent } from './performance/performance.component';
import { AppComponent } from './app.component';


@NgModule({
  exports:  [
    CdkTableModule,
    CdkTreeModule,
    MatAutocompleteModule,
    MatBadgeModule,
    MatBottomSheetModule,
    MatButtonModule,
    MatButtonToggleModule,
    MatCardModule,
    MatCheckboxModule,
    MatChipsModule,
    MatStepperModule,
    MatDatepickerModule,
    MatDialogModule,
    MatDividerModule,
    MatExpansionModule,
    MatGridListModule,
    MatIconModule,
    MatInputModule,
    MatListModule,
    MatMenuModule,
    MatNativeDateModule,
    MatPaginatorModule,
    MatProgressBarModule,
    MatProgressSpinnerModule,
    MatRadioModule,
    MatRippleModule,
    MatSelectModule,
    MatSidenavModule,
    MatSliderModule,
    MatSlideToggleModule,
    MatSnackBarModule,
    MatSortModule,
    MatTableModule,
    MatTabsModule,
    MatToolbarModule,
    MatTooltipModule,
    MatTreeModule
    ]
})
export class MyMaterialModule {}

const appRoutes: Routes = [
  { path: 'home',                            component:  HomeComponent},
  { path: 'search',                       component:  SearchUiComponent},
  { path: 'project_description',          component:  ProjectDescriptionComponent},
  { path: 'performance',                  component:  PerformanceComponent},
  { path: 'all_sentence',                 component:  AllSentenceComponent},
  { path: '**',
    redirectTo: 'home',
    pathMatch: 'full'
  }
];


@NgModule({
  imports:      [ BrowserModule, FormsModule, BrowserAnimationsModule, MyMaterialModule ,
                 MatNativeDateModule, HttpClientModule,
                 RouterModule.forRoot(
                   appRoutes,
                   { enableTracing: true } // <-- debugging purposes only
                 ) ],
  declarations: [ AppComponent, SearchUiComponent, ProjectDescriptionComponent,
                  AllSentenceComponent, HomeComponent, PerformanceComponent ],
  bootstrap:    [ AppComponent ],
  providers:    [ myHttpService, {provide: APP_BASE_HREF, useValue : '/' }]
})
export class AppModule { }
