---
title: Controlla il formato numero personalizzato quando imposti Style.Custom Property
type: docs
weight: 160
url: /it/java/check-custom-number-format-when-setting-style-custom-property/
---

## **Possibili Scenari di Utilizzo**

Se assegni un formato numerico personalizzato non valido alla proprietà [**Style.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) allora Aspose.Cells non genererà alcuna eccezione. Ma se vuoi che Aspose.Cells verifichi se il formato numerico personalizzato assegnato è valido o no, imposta la proprietà [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) su **true**.

## **Controlla il Formato Numero Personalizzato durante l'impostazione della Proprietà Stile Personalizzato**

Il seguente codice di esempio assegna un formato numerico personalizzato non valido alla proprietà [**Style.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom). Poiché abbiamo già impostato la proprietà [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) su **true**, quindi l'API genererà un'eccezione CellsException ad es. *Formato numero non valido*.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CheckCustomNumberFormat-CheckCustomNumberFormat.java" >}}
{{< app/cells/assistant language="java" >}}
