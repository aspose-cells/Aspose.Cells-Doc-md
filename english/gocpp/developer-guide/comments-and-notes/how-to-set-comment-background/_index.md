---
title: How to change background in comment in Excel with Golang via C++
linktitle: Comment Background
type: docs
weight: 190
url: /go-cpp/how-to-set-comment-background/
description: How to change color in comment in Excel. How to insert picture or image in comment in Excel using C++.
keywords: add inset picture image color comment background excel
---

{{% alert color="primary" %}}

Comments are added to cells to record comments, anything from the details of how a formula is worked, where a value comes from, or questions from reviewers. Comments play an extremely important role when multiple people discuss or review the same document at different times. How to distinguish different people's comments? Yes, we can set a different background color for each comment. But when we need to process a lot of documents and a lot of comments, doing it manually is a disaster. Fortunately, [**Aspose.Cells**](https://products.aspose.com/cells/go-cpp/) provides an API that allows you to do this in code.

{{% /alert %}}

## **How to change color in comment in Excel**

When you don't need the default background color for comments, you may want to replace it with a color you're interested in. How do I change the background color of the Comments box in Excel?

The following code will guide you on how to use [**Aspose.Cells**](https://products.aspose.com/cells/go-cpp/) to add your favorite background color to comments of your own choice.

Here we have prepared a [sample file](exmaple.xlsx) for you. This file is used to initialize the Workbook object in the code below.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetCommentBackground.go" >}}
Execute the above code, and you will get an [output file](result.xlsx).

## **How to insert picture or image in comment in Excel**

Microsoft Excel lets users customize the look and feel of spreadsheets to a great extent. It is even possible to add background pictures to comments. Adding a background image can be an aesthetic choice or be used to strengthen branding.

The sample code below creates an XLSX file from scratch using [**Aspose.Cells**](https://products.aspose.com/cells/go-cpp/) API, and adds a comment with a picture background to cell A1.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetCommentBackground-1.go" >}}