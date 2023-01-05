---
title: Controlla il formato numerico personalizzato durante l'impostazione di Style.Custom Property
type: docs
weight: 160
url: /it/java/check-custom-number-format-when-setting-style-custom-property/
---
## **Possibili scenari di utilizzo**

 Se assegni un formato numerico personalizzato non valido a[**Stile.Personalizzato**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom)property quindi Aspose.Cells non genererà alcuna eccezione. Ma se vuoi che Aspose.Cells controlli se il formato del numero personalizzato assegnato è valido o meno, imposta il[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) proprietà a**VERO**.

## **Controllare il formato numero personalizzato durante l'impostazione della proprietà Style.Custom**

 Il seguente codice di esempio assegna un formato numerico personalizzato non valido a[**Stile.Personalizzato**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) proprietà. Dal momento che abbiamo già impostato[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) proprietà a**VERO** , quindi API genererà CellsException ad es*Formato numerico non valido*.

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CheckCustomNumberFormat-CheckCustomNumberFormat.java" >}}
