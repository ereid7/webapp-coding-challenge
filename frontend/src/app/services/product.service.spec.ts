import { inject, TestBed } from '@angular/core/testing';
import {
  HttpClientTestingModule,
  HttpTestingController
} from "@angular/common/http/testing"
import { ProductService } from './product.service';

describe('ProductService', () => {
  let productService: ProductService;
  let httpTestingController: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule]
    });
    httpTestingController = TestBed.get(HttpTestingController);
    productService = TestBed.inject(ProductService);
  });

  beforeEach(inject(
    [ProductService],
    (service: ProductService) => {
      productService = service;
    }
  ));

  it('should be created', () => {
    expect(productService).toBeTruthy();
  });

  it('should return data on get request', () => {
    const req = httpTestingController.expectOne({
      method: "GET",
      url: productService.apiUri
    })
    var mockProducts = [
      {
        name: 'testProduct',
        ingredients: ['ingredient1', 'ingredient2']
      },
      {
        name: 'testProduct2',
        ingredients: ['ingredient3', 'ingredient4']
      },
    ]

    req.flush(mockProducts);
    expect(productService.productList[0]).toEqual(mockProducts[0])
  });

  it('should call getProducts when product is created', () => {
    var mockProductName = 'mockProductName'
    var mockIngredients = ['mockIngredient1', 'mockIngredient2']
    var spy = spyOn(productService, 'getProducts')
    productService.createProduct('mockProductName', ['mockIngredient1', 'mockIngredient2'])
    const req = httpTestingController.expectOne({
      method: "PUT",
      url: `${productService.apiUri}?name=${mockProductName}&ingredients=${mockIngredients.toString()}`
    })
    req.flush(200)

    expect(spy).toHaveBeenCalled()
  });
});
