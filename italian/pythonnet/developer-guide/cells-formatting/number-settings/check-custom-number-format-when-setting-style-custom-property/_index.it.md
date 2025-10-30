---
title: Controlla il formato numero personalizzato quando imposti Style.Custom Property
description: Aspose.Cells è una libreria Python per lavorare con file di fogli di calcolo, che supporta il controllo dei formati numerici personalizzati durante la formattazione. Questo articolo mostrerà come usare la libreria Aspose.Cells per verificare i formati numerici personalizzati per assicurarsi che la formattazione sia corretta.
keywords: Aspose.Cells, librerie Python, fogli di calcolo, formattazione, formattazione numerica personalizzata, verifica, convalida
type: docs
weight: 170
url: /it/python-net/check-custom-number-format-when-setting-style-custom-property/
---

## **Possibili Scenari di Utilizzo**

Se si assegna un formato numero personalizzato non valido a [**Style.custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom) proprietà, allora Aspose.Cells non genererà alcuna eccezione. Ma se si desidera che Aspose.Cells verifichi se il formato numero personalizzato assegnato è valido o meno, si prega di impostare la proprietà [**Workbook.settings.check_custom_number_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_custom_number_format/) su **true**.

## **Controlla il formato numero personalizzato quando si imposta la proprietà Style.Custom**

Il seguente codice di esempio assegna un formato numero personalizzato non valido alla proprietà [**Style.custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom). Poiché abbiamo già impostato la proprietà [**Workbook.settings.check_custom_number_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_custom_number_format/) su **true**, quindi genera un'eccezione ad esempio Formato numero non valido. Si prega di leggere i commenti all'interno del codice per ulteriori informazioni.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-CheckCustomFormatPattern.py" >}}

{{< app/cells/assistant language="python-net" >}}
