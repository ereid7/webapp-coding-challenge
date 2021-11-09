import { Component, Input, OnInit } from '@angular/core';
import { ProductService } from '../services/product.service';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {

  ingredients: string[] = []
  ingredientName: string = ''

  constructor(public productService: ProductService) {
  }

  onKey(event: any) {const inputValue = event.target.value;}

  ngOnInit(): void {
  }

}
