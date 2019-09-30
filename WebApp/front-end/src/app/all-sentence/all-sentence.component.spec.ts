import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AllSentenceComponent } from './all-sentence.component';

describe('AllSentenceComponent', () => {
  let component: AllSentenceComponent;
  let fixture: ComponentFixture<AllSentenceComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AllSentenceComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AllSentenceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
