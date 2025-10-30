---
title: Skicka form framåt eller bak i arbetsbladet med Golang via C++
linktitle: Skicka form framåt eller bakåt inne i Arbetsbladet
type: docs
weight: 3400
url: /sv/go-cpp/send-shape-front-or-back-inside-the-worksheet/
description: Lär dig hur du ändrar z ordningen för figurer i ett arbetsblad med API Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

När flera former finns på samma plats bestäms deras synlighet av deras z-order-placeringar. Aspose.Cells tillhandahåller [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/go-cpp/shape/tofrontorback/)-metoden, som ändrar formen z-ordningsposition. Om du vill skicka en form till bakgrunden använder du ett negativt nummer som -1, -2, -3 etc. Om du vill föra en form till fronten använder du ett positivt nummer som 1, 2, 3 etc.

## **Skicka form framåt eller bakåt inne i Arbetsbladet**

Följande exempel visar användningen av [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/go-cpp/shape/tofrontorback/)-metoden. Se [exempel-Excelfilen](50528330.xlsx) som används i koden och den [utdata-Excelfil](50528331.xlsx) som genereras. Skärmbilden visar effekten av koden på exempel-Excelfilen vid körning.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SendShapeFrontOrBackInsideTheWorksheet.go" >}}
