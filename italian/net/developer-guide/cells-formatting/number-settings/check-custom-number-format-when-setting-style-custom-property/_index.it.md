---
title: Controlla il formato numero personalizzato quando imposti Style.Custom Property
description: Aspose.Cells è una libreria .NET per lavorare con file di fogli di calcolo, che supporta il controllo dei formati numerici personalizzati durante lo styling. Questo articolo ti mostrerà come utilizzare la libreria Aspose.Cells per controllare i formati numerici personalizzati per garantire che lo styling sia corretto.
keywords: Aspose.Cells, librerie NET, fogli di calcolo, styling, formattazione numerica personalizzata, controllo, convalida
type: docs
weight: 170
url: /it/net/check-custom-number-format-when-setting-style-custom-property/
---

## **Possibili Scenari di Utilizzo**

Se si assegna un formato numero personalizzato non valido a [**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) proprietà, allora Aspose.Cells non genererà alcuna eccezione. Ma se si desidera che Aspose.Cells verifichi se il formato numero personalizzato assegnato è valido o meno, si prega di impostare la proprietà [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) su **true**.

## **Controlla il formato numero personalizzato quando si imposta la proprietà Style.Custom**

Il seguente codice di esempio assegna un formato numero personalizzato non valido alla proprietà [**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom). Poiché abbiamo già impostato la proprietà [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) su **true**, quindi genera un'eccezione ad esempio Formato numero non valido. Si prega di leggere i commenti all'interno del codice per ulteriori informazioni.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
