import { Component } from '@angular/core';
import { MatDialog } from '@angular/material/dialog'
import { CreateProductDialogComponent } from './create-product-dialog/create-product-dialog.component';
import { ProductService } from './services/product.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'coding-challenge';

  constructor(private dialog: MatDialog) { }

  openDialog() {
    const dialogRef = this.dialog.open(CreateProductDialogComponent,{});

  }
}
