import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {
  constructor(private _http: HttpClient, private _router: Router, private _activatedRoute: ActivatedRoute) {
  }
  userData: {
    userName: string,
    firstName: string,
    lastName: string
  }
  postUrl = 'http://localhost:4200/'

  ngOnInit(): void {

  }

  submit(userData: any) {
    console.log(userData);
    const body = {
      userName: userData.form.controls.userName.value,
      firstName: userData.form.controls.firstName.value,
      lastName: userData.form.controls.lastName.value
    };
    this._http.post(this.postUrl, body);
  }
  navigateToUsers() {
    this._router.navigate(['view-users'], { relativeTo: this._activatedRoute })
  }
}
