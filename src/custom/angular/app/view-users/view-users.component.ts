import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-view-users',
  templateUrl: './view-users.component.html',
  styleUrls: ['./view-users.component.css']
})
export class ViewUsersComponent implements OnInit {
  getUrl = 'https://placeUrl';
  map = new Map();
  map1= new Array();
  sampleData = {
    "userName1": { firstName: 'User1FirstName', lastName: 'User1LastName' },
    "userName2": { firstName: 'User2FirstName', lastName: 'User2LastName' },
    "userName3": { firstName: 'User3FirstName', lastName: 'User3LastName' },
    "userName4": { firstName: 'User3FirstName', lastName: 'User3LastName' },
  }
  constructor(private http: HttpClient, private _router: Router, private _activatedRoute: ActivatedRoute) { }

  ngOnInit() {
    // this.getData().subscribe((value:any) => {
    //   const keys = Object.keys(value);
    //   keys.forEach((key) => {
    //     this.map.set(value[key], { firstName: value[key].firstName, lastName: value[key].lastName, });
    //   });
    // });
    const userKeys = Object.keys(this.sampleData);
    let data: any;
    data = this.sampleData;
    userKeys.forEach((key) => {
      this.map.set(data[key], { firstName: data[key].firstName, lastName: data[key].lastName,});
    })
  }
  getData() {
    return this.http.get(this.getUrl);
  }
  navigateBack(){
   this._router.navigate(['']);
  }
}
