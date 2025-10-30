---
title: Controlla il formato numero personalizzato quando imposti Style.Custom Property
linktitle: Controlla il formato numero personalizzato quando imposti Style.Custom Property
description: Aspose.Cells è una libreria Node.js per lavorare con file di fogli di calcolo, che supporta la verifica dei formati numerici personalizzati durante lo stile. Questo articolo mostrerà come usare la libreria Aspose.Cells per verificare i formati numerici personalizzati e assicurarsi che lo stile sia corretto.
keywords: Aspose.Cells, librerie Node.js, fogli di calcolo, stilizzazione, formattazione numerica personalizzata, verifica, validazione
type: docs
weight: 170
url: /it/nodejs-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Possibili Scenari di Utilizzo**

Se assegni un formato numerico personalizzato non valido al metodo [**Style.setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-), allora Aspose.Cells for Node.js via C++ non lancerà eccezioni. Ma se vuoi che Aspose.Cells verifichi se il formato numerico personalizzato assegnato è valido o meno, imposta il metodo [**Workbook.getSettings().setCheckCustomNumberFormat(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setCheckCustomNumberFormat-boolean-) su **true**.

## **Verifica del formato numerico personalizzato durante l'impostazione del metodo Style.setCustom(string)**

Il codice di esempio seguente assegna un formato numerico personalizzato non valido al metodo [**Style.setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-). Poiché abbiamo già impostato il metodo [**Workbook.getSettings().setCheckCustomNumberFormat(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setCheckCustomNumberFormat-boolean-) su **true**, genera un'eccezione, ad esempio Numero non valido. Leggi i commenti nel codice per ulteriori dettagli.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-CheckCustomNumberFormat.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
