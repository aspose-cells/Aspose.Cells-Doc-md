---
title: GridCell Yorumları Oluştur, Kaldır ve Al
type: docs
weight: 10
url: /tr/java/create-remove-and-get-gridcell-comments/
---

## **Olası Kullanım Senaryoları**
Aşağıdaki makale, GridWeb çalışma sayfasında GridCell yorumları oluşturmayı, kaldırmayı ve almayı açıklar. GridWeb, fareyi hücrenin üzerine getirdiğinizde MS-Excel gibi yorumları bir İpucu olarak görüntüler, bu ekran görüntüsünde gösterildiği gibi.

![todo:image_alt_text](create-remove-and-get-gridcell-comments_1.png)
## **Hücre İçinde Yorum Objesi Oluştur**
Lütfen hücre içinde bir yorum objesi oluşturmak için GridCell.CreateComment yöntemini kullanın. Aşağıdaki örnek kod, GridWeb'in ilk çalışma sayfasının B4 hücresine bir örnek yorum oluşturur.

{{< highlight java >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Create comment with these parameters

// i.e. note, author, isvisible

cell.createComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **Hücreden Yorum Objesi Kaldır**
Lütfen hücreden bir yorum objesi kaldırmak için GridCell.RemoveComment yöntemini kullanın. Aşağıdaki örnek kod, GridWeb'in ilk çalışma sayfasındaki B4 hücresinden yorumu kaldırır.



{{< highlight java >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Remove the comment object from this cell.

cell.removeComment();

{{< /highlight >}}
## **Hücreden Yorum Objesini Al**
Lütfen hücreden yorum objesini almak için GridCell.GetComment() yöntemini kullanın. Aşağıdaki örnek kod, B4 hücresinden yorum objesini alır ve ardından Yazar, Not, Görünürlük vb. gibi çeşitli özelliklerine erişir.

{{< highlight java >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Get comment of this cell

GridComment gridComm = cell.getComment();

// Access its various properties

String strAuth = gridComm.getAuthor();

String strNote = gridComm.getNote();

boolean isVis = gridComm.isVisible();


{{< /highlight >}}




