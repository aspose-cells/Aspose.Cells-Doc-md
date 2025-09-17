##Reusing Style Objects
In Aspose.Cells for Node.js via C++, by creating and using reusable style objects, you can simplify style management and improve code efficiency. Our guide will help you leverage the advantages of reusable style objects and implement them in your application.
Reusing style objects can save memory and make a program faster.
To apply some formatting to a large range of cells in a worksheet:
1. Create a style object.
1. Specify the attributes.
1. Apply the style to the cells in the range.
Because the [**Cell.getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) / [**Cell.setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) approach uses a lot less memory, and is efficient, the older Cell.style property which consumed a lot of unnecessary memory was removed with the release of Aspose.Cells 7.1.0.
