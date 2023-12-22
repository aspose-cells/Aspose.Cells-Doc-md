---
title: Controlla il formato del numero personalizzato quando imposti la proprietà Style.Custom
description: Aspose.Cells è una libreria .NET per lavorare con file di fogli di calcolo, che supporta il controllo dei formati di numeri personalizzati durante lo styling. Questo articolo ti mostrerà come utilizzare la libreria Aspose.Cells per controllare i formati dei numeri personalizzati per garantire che lo stile sia corretto.
keywords: Aspose.Cells, NET libraries, spreadsheets, styling, custom number formatting, checking, validation
type: docs
weight: 170
url: /it/net/check-custom-number-format-when-setting-style-custom-property/
---
##  **Possibili scenari di utilizzo**

 Se assegni un formato numero personalizzato non valido a[**Stile.Personalizzato**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) proprietà, allora Aspose.Cells non genererà alcuna eccezione. Ma se vuoi che Aspose.Cells controlli se il formato del numero personalizzato assegnato è valido o meno, allora imposta il[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) proprietà su *true**.

##  **Controlla il formato numero personalizzato quando imposti la proprietà Style.Custom**

 Il seguente codice di esempio assegna un formato numero personalizzato non valido a[**Stile.Personalizzato**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) proprietà. Da allora, abbiamo già impostato[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) proprietà su *true**, pertanto genera un'eccezione, ad esempio formato numero non valido. Si prega di leggere i commenti all'interno del codice per ulteriore aiuto.

##  **Codice d'esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
