---
title: Specificare i Separatori Decimali e di Gruppo Personalizzati per il Workbook
linktitle: Specificare i Separatori Decimali e di Gruppo Personalizzati per il Workbook
type: docs
weight: 110
url: /it/nodejs-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Modifica i separatori decimali e di gruppo dei numeri in Excel utilizzando Aspose.Cells for Node.js via C++. 
keywords: specifica separatore decimale personalizzato in excel node.js tramite C++, specifica separatore di gruppo personalizzato in excel node.js tramite C++, modifica separatore decimale e di gruppo in excel node.js tramite C++
---

{{% alert color="primary" %}}

In Microsoft Excel, è possibile specificare i separatori decimali e migliaia personalizzati invece di utilizzare i separatori di sistema dalle **Opzioni Avanzate di Excel** come mostrato nella schermata sottostante.

Aspose.Cells fornisce i metodi [**WorkbookSettings.setNumberDecimalSeparator(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setNumberDecimalSeparator-string-) e [**WorkbookSettings.setNumberGroupSeparator(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setNumberGroupSeparator-string-) per impostare i separatori personalizzati per formattare/parsing i numeri.

{{% /alert %}}

## **Specificare i Separatori Personalizzati utilizzando Microsoft Excel**

La seguente schermata mostra le **Opzioni Avanzate di Excel** e evidenzia la sezione per specificare i **Separatori Personalizzati**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Specificare separatori personalizzati usando Aspose.Cells for Node.js via C++**

Il seguente codice di esempio illustra come specificare i separatori personalizzati utilizzando l'API Aspose.Cells. Specifica i separatori personalizzati per il numero decimale e per il raggruppamento come rispettivamente punto e spazio.

### Codice Node.js per specificare separatori decimali e di gruppo personalizzati per i numeri

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-SpecifyCustomNumberDecimalAndGroupSeparators.js" >}}


{{< app/cells/assistant language="nodejs-cpp" >}}
