---
title: GridCell Yorumları Oluştur, Kaldır ve Al
type: docs
weight: 100
url: /tr/net/aspose-cells-gridweb/manage-comment/
keywords: GridWeb,comment
description: Bu makale, GridWeb deki yorumlarla çalışmayı tanıtıyor.
---

## **Olası Kullanım Senaryoları**
Aşağıdaki makale, GridWeb çalışma sayfasında hücreden (GridCell) yorum oluşturmayı, kaldırmayı ve almayı nasıl açıklar. GridWeb, hücreye fareyi hücre üzerine getirdiğinizde MS-Excel gibi Tooltip gösterir. Ekran görüntüsünde gösterildiği gibi.

![todo:image_alt_text](create-remove-and-get-gridcell-comments_1.png)
## **Hücre İçinde Yorum Objesi Oluştur**
Lütfen hücre içinde bir yorum objesi oluşturmak için GridCell.CreateComment yöntemini kullanın. Aşağıdaki örnek kod, GridWeb'in ilk çalışma sayfasının B4 hücresine bir örnek yorum oluşturur.

{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Create comment with these parameters

//i.e. note, author, isvisible

cell.CreateComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **Hücreden Yorum Objesi Kaldır**
Lütfen, bir hücreden yorum objesini kaldırmak için GridCell.RemoveComment yöntemini kullanın. Aşağıdaki örnek kod, GridWeb'in ilk çalışsayfasındaki B4 hücresinden yorumu kaldırır.



{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Remove the comment object from this cell.

cell.RemoveComment();

{{< /highlight >}}
## **Hücreden Yorum Objesini Al**
Lütfen, hücreden yorum objesini almak için GridCell.GetComment() yöntemini kullanın. Aşağıdaki örnek kod, B4 hücresinden yorum objesini alır ve ardından Yazar, Not, Görünürlük vb. gibi çeşitli özelliklerine erişir.

{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Get comment of this cell

GridComment gridComm = cell.GetComment();

//Access its various properties

string strAuth = gridComm.Author;

string strNote = gridComm.Note;

bool isVis = gridComm.IsVisible;

{{< /highlight >}}
