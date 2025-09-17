##Reusing Style Objects with Golang via C++
In Aspose.Cells for C++, by creating and using reusable style objects, you can simplify style management and improve code efficiency. Our guide will help you leverage the advantages of reusable style objects and implement them in your application.
Reusing style objects can save memory and make a program faster.
To apply some formatting to a large range of cells in a worksheet:
1. Create a style object.
1. Specify the attributes.
1. Apply the style to the cells in the range.
Because the [**Cell.GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/)/[**Cell.SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) approach uses a lot less memory, and is efficient, the older Cell.Style property which consumed a lot of unnecessary memory, was removed with the release of Aspose.Cells 7.1.0.
