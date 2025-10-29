---
title: Добавление закладок PDF с именованными назначениямии с помощью Golang через C++
linktitle: Добавление закладок PDF с именованными местами назначения
type: docs
weight: 20
url: /ru/go-cpp/add-pdf-bookmarks-with-named-destinations/
description: Узнайте, как добавлять закладки PDF с именованными назначениями с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Именованные назначения — это особый тип закладок или ссылок в PDF, которые не зависят от страниц PDF. Это означает, что если страницы в PDF добавляются или удаляются, закладки могут стать недействительными, а именованные назначения останутся целыми. Чтобы создать именованное назначение, установите свойство [**PdfBookmarkEntry.GetDestinationName()**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/getdestinationname/).

## **Добавление закладок PDF с именованными местами назначения**

Пожалуйста, обратитесь к следующему образцу кода, его [исходному файлу Excel](50528348.xlsx) и [выходному файлу PDF](50528349.pdf). Снимок экрана показывает закладки и именованные места в выходном PDF. На снимке также описано, как просматривать именованные места и что для этого требуется профессиональная версия Acrobat Reader.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddPdfBookmarksWithNamedDestinations.go" >}}
