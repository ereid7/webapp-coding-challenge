import { Component, OnInit, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { ProductService } from '../services/product.service';

@Component({
  selector: 'app-create-product-dialog',
  templateUrl: './create-product-dialog.component.html',
  styleUrls: ['./create-product-dialog.component.css']
})
export class CreateProductDialogComponent implements OnInit {

  productName: string = ''
  ingredientList: string[] = []
  ingredient: string = ''
  createEnabled: boolean = false

  constructor(
    @Inject(MAT_DIALOG_DATA) private data: any,
    private dialogRef: MatDialogRef<CreateProductDialogComponent>,
    public productService: ProductService) {

  }

  public addIngredient() {
    if (this.ingredient) {
      this.ingredientList.push(this.ingredient)
      this.ingredient = ''
    }
  }

  public createProduct() {
    if (this.productName) {
      this.productService.createProduct(this.productName, this.ingredientList)

      this.productName = ''
      this.ingredientList = []
    }

    this.dialogRef.close()
  }

  ngOnInit(): void {
  }
}
