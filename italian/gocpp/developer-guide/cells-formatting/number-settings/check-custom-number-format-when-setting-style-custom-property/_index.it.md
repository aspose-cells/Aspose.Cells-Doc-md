---
title: Verifica il Formato Numerico Personalizzato quando Imposti la Proprietà Style.Custom con Golang tramite C++
description: Aspose.Cells è una libreria C++ per la gestione di file di fogli di calcolo, che supporta la verifica dei formati numerici personalizzati durante la formattazione. Questo articolo mostrerà come usare la libreria Aspose.Cells per controllare i formati numerici personalizzati e garantire che la formattazione sia corretta.
keywords: Aspose.Cells, librerie C++, fogli di calcolo, formattazione, formato numerico personalizzato, verifica, validazione
type: docs
weight: 170
url: /it/go-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Possibili Scenari di Utilizzo**

Se assegni un formato numerico personalizzato non valido alla proprietà [**Style.GetCustom()**](https://reference.aspose.com/cells/go-cpp/style/getcustom/), Aspose.Cells non genererà eccezioni. Ma se desideri che Aspose.Cells verifichi se il formato numerico personalizzato assegnato è valido o meno, imposta la proprietà [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) su **true**.

## **Controlla il formato numero personalizzato quando si imposta la proprietà Style.Custom**

Il seguente esempio di codice assegna un formato numerico personalizzato non valido alla proprietà [**Style.GetCustom()**](https://reference.aspose.com/cells/go-cpp/style/getcustom/). Poiché abbiamo già impostato la proprietà [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) su **true**, verrà generata un'eccezione, ad esempio Formato numerico non valido. Leggi i commenti nel codice per ulteriori dettagli.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CheckCustomNumberFormatWhenSettingStyleCustomProperty.go" >}}
