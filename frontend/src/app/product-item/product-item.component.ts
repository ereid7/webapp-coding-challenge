import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent implements OnInit {

  @Input() ingredients: [] = []
  @Input() name: string = ''
  @Input() id: number = -1;

  constructor() { }

  ngOnInit(): void {
  }
}
