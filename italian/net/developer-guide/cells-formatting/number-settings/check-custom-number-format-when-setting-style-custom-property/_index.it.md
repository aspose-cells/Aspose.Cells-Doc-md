---
title: Controlla il formato numerico personalizzato durante l'impostazione di Style.Custom Property
type: docs
weight: 170
url: /it/net/check-custom-number-format-when-setting-style-custom-property/
---
## **Possibili scenari di utilizzo**

 Se assegni un formato numerico personalizzato non valido a[**Stile.Personalizzato**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)property, quindi Aspose.Cells non genererà alcuna eccezione. Ma se vuoi che Aspose.Cells controlli se il formato del numero personalizzato assegnato è valido o meno, imposta il[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) proprietà a**VERO**.

## **Controllare Formato numero personalizzato quando si imposta la proprietà Style.Custom**

 Il seguente codice di esempio assegna un formato numerico personalizzato non valido a[**Stile.Personalizzato**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) proprietà. Da allora, abbiamo già impostato[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) proprietà a**VERO**, quindi genera un'eccezione, ad esempio Formato numerico non valido. Si prega di leggere i commenti all'interno del codice per ulteriore aiuto.

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
