---
title: Kopiera områden av Excel
linktitle: Kopiera områden
type: docs
weight: 105
url: /sv/python-net/copy-ranges-of-excel/
description: Denna artikel beskriver hur du kopierar områden i Excel med Aspose.Cells för Python via .NET biblioteket.
keywords: Python Excel Library, Python Så här kopierar du områden i Excel, Python Så här kopierar du endast områdesdata med python excel biblioteket, Python så här klistrar du in området med alternativ, Python så här kopierar du endast data för området.
---

## **Introduktion**

I Excel kan du markera ett område, kopiera området och sedan klistra in det med specifika alternativ på samma arbetsblad, andra arbetsblad eller andra filer.

## **Kopiera områden med hjälp av Aspose.Cells för Python Excel-biblioteket**

Aspose.Cells för Python via .NET tillhandahåller några överbelastning [**Range.copy**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy/#aspose.cells.Range)-metoder för att kopiera området.
Och [**Range.copy_style**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy_style/#aspose.cells.Range) endast kopieringsstilen för området; [**Range.copy_data**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy_data/#aspose.cells.Range) endast kopieringsvärdet för området

## **Kopiera område**

Skapa två områden: källområdet, målområdet, sedan kopiera källområdet till målområdet med [**Range.copy**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy/#aspose.cells.Range)-metoden.

Se följande kod:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Copy-Range.py" >}}

## **Klistra in område med alternativ**

Aspose.Cells för Python via .NET stöder att klistra in området med specifik typ.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Paste-Range.py" >}}

## **Endast kopiera data för området**
Du kan också kopiera datan med [**Range.copy_data**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy_data/#aspose.cells.Range)-metoden enligt följande koder:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Copy-Range-Data.py" >}}

## **Fortsatta ämnen**
- [Kopiera radhöjder från källspann till destinationspann](/cells/sv/python-net/copy-row-heights-of-source-range-to-destination-range/)


