import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  
  productList: any[] = []
  apiUri: string = 'http://127.0.0.1:5000'

  constructor(private http: HttpClient) {
    this.getProducts()
  }

  public getProducts() {
    this.http.get(this.apiUri)
      .subscribe(data => {
        this.productList = (data as any[]).sort((a, b) => a - b);
      });
  }

  public createProduct(productName: string, ingredients: string[]) {
    let url = `${this.apiUri}?name=${productName}&ingredients=${ingredients.toString()}`
    this.http.put(url, {})
      .subscribe(data => {

        // fetch all products after product created
        this.getProducts();
      })
  }
}
