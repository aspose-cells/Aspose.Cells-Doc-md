---
title: How to change background in comment in Excel with Node.js via C++
linktitle: Comment Background
type: docs
weight: 190
url: /nodejs-cpp/how-to-set-comment-background/
description: How to change color in comment and insert picture or image in comment in Excel using Aspose.Cells for Node.js via C++.
keywords: add inset picture image color comment background excel Node.js via C++
---

{{% alert color="primary" %}}
Comments are added to cells to record comments, anything from the details of how a formula is worked, where a value comes from or questions from reviewers. Comments play an extremely important role when multiple people discuss or review the same document at different times. How to distinguish different people's comments? Yes, we can set a different background color for each comment. But when we need to process a lot of documents and a lot of comments, doing it manually is a disaster. Fortunately [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/) provides an API that allows you to do this in code.
{{% /alert %}}

## **How to change color in comment in Excel**

When you don't need the default background color for comments, you may want to replace it with a color you're interested in. How do I change the background color of the Comments box in Excel?

The following code will guide you how to use [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/) to add your favorite background color to comments of your own choice.

Here we have prepared a [sample file](exmaple.xlsx) for you. This file is used to initialize the Workbook object in the code below.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Initialize a new workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "example.xlsx"));

// Accessing the newly added comment
const comment = workbook.getWorksheets().get(0).getComments().get(0);

// change background color
const shape = comment.getCommentShape();
shape.getFill().getSolidFill().setColor(AsposeCells.Color.Red);

// Save the Excel file
workbook.save(path.join(dataDir, "result.xlsx"));
```

Execute the above code and you will get an [output file](result.xlsx).

## **How to insert picture or image in comment in Excel**

Microsoft Excel lets users customize the look and feel of spreadsheets to a great extent. It is even possible to add background pictures to comments. Adding a background image can be an aesthetic choice or be used to strengthen branding.

The sample code below creates an XLSX file from scratch using [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/) API, and adds a comment with a picture background to cell A1.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
if (!require("fs").existsSync(dataDir)) {
    require("fs").mkdirSync(dataDir);
}

// Instantiate a Workbook
const workbook = new AsposeCells.Workbook();

// Get a reference of comments collection with the first sheet
const comments = workbook.getWorksheets().get(0).getComments();

// Add a comment to cell A1
const commentIndex = comments.add(0, 0);
const comment = comments.get(commentIndex);
comment.setNote("First note.");
comment.getFont().setName("Times New Roman");

// Load an image into stream
const fs = require("fs");
const bmp = fs.readFileSync(path.join(dataDir, "image2.jpg"));
const ms = Buffer.from(bmp);

// Set image data to the shape associated with the comment
comment.getCommentShape().getFill().getImageData().setData(ms);

// Save the workbook
const outputFilePath = path.join(dataDir, "commentwithpicture1.out.xlsx");
workbook.save(outputFilePath, AsposeCells.SaveFormat.Xlsx);
```

