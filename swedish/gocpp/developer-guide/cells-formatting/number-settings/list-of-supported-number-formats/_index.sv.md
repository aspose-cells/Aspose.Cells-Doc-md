---
title: Lista över stödda nummerformat med Golang via C++
description: Aspose.Cells är ett C++ bibliotek för att bearbeta kalkylbladsfiler, vilket stöder ett antal nummerformat. Den här artikeln ger en lista på stödda nummerformat så att användare kan välja rätt format enligt sina behov.
keywords: Aspose.Cells, C++ bibliotek, kalkylblad, nummerformat, lista, stödjer
type: docs
weight: 30
url: /sv/go-cpp/list-of-supported-number-formats/
---

## **Aspose.Cells**
Aspose.Cells-komponenten erbjuder några inbyggda nummerformat för att konfigurera visningsformaten för nummer och datum. Dessa inbyggda nummerformat kan tillämpas genom att använda **Number**-egenskapen på **Style**-objektet. Alla inbyggda nummerformat ges unika numeriska värden. Utvecklare kan tilldela valfritt numeriskt värde till *Number*-egenskapen hos **Style**-objektet och därmed tillämpas visningsformatet. Det här tillvägagångssättet är snabbare. De inbyggda nummerformat som stöds av Aspose.Cells-komponenten ges nedan:

|**Värde**|**Typ**|**Formatsträng**|
| :- | :- | :- |
|0 |General |General |
|1 |Decimal |0 |
|2 |Decimal |0.00 |
|3 |Decimal |#,##0 |
|4 |Decimal |#,##0.00 |
|5 |Currency |$#,##0;$-#,##0 |
|6 |Currency |$#,##0;$-#,##0 |
|7 |Currency |$#,##0.00;$-#,##0.00 |
|8 |Currency |$#,##0.00;$-#,##0.00 |
|9 |Percentage |0% |
|10 |Percentage |0.00% |
|11 |Scientific |0.00E+00 |
|12 |Fraction |# ?/? |
|13 |Fraction |# */*|
|14 |Date |m/d/yy |
|15 |Date |d-mmm-yy |
|16 |Date |d-mmm |
|17 |Date |mmm-yy |
|18 |Time |h:mm AM/PM |
|19 |Time |h:mm:ss AM/PM |
|20 |Time |h:mm |
|21 |Time |h:mm:ss |
|22 |Time |m/d/yy h:mm |
|37 |Currency |#,##0;-#,##0 |
|38 |Currency |#,##0;-#,##0 |
|39 |Currency |#,##0.00;-#,##0.00 |
|40 |Currency |#,##0.00;-#,##0.00 |
|41 |Accounting |_ * #,##0_ ;_ * "_ ;_ @_ |
|42 |Accounting |_ $* #,##0_ ;_ $* "_ ;_ @_ |
|43 |Accounting |_ * #,##0.00_ ;_ * "??_ ;_ @_ |
|44 |Accounting |_ $* #,##0.00_ ;_ $* "??_ ;_ @_ |
|45 |Time |mm:ss |
|46 |Time |h :mm:ss |
|47 |Time |mm:ss.0 |
|48 |Scientific |##0.0E+00 |
|49 |Text |@ |

## **Aspose.Cells Grid Suite**
Som vi vet finns det två Aspose.Cells Grid-kontroller: Aspose.Cells.GridDesktop & Aspose.Cells.GridWeb. Båda kontrollerna stödjer ett stort antal nummerformat, som är uppdelade i två avsnitt med avseende på varje kontroll enligt följande:

- Nummerformat som stöds i Aspose.Cells.GridDesktop
- Nummerformat som stöds i Aspose.Cells.GridWeb

### **Nummerformat som stöds i Aspose.Cells.GridDesktop**
Aspose.Cells.GridWeb stödjer också 59 typer av nummerformat som listas nedan:

|**Index**|**Nummerformat**|
| :- | :- |
|0 |General |
|1 |0 |
|2 |0.00 |
|3 |#,##0 |
|4 |#,##0.00 |
|5 |\"$\"#,##0_);(\"$\"#,##0) |
|6 |\"$\"#,##0_);(\"$\"#,##0) |
|7 |\"$\"#,##0.00_);(\"$\"#,##0.00) |
|8 |\"$\"#,##0.00;\"$\"-#,##0.00 |
|9 |0% |
|10 |0.00% |
|11 |0.00E+00 |
|12 |#?/? |
|13 |# */*|
|14 |m/d/yy |
|15 |d-mmm-yy |
|16 |d-mmm |
|17 |mmm-yy |
|18 |h:mm AM/PM |
|19 |h:mm:ss AM/PM |
|20 |h:mm |
|21 |h:mm:ss |
|22 |m/d/yy h:mm |
|23 |\"$\"#,##0;(\"$\"#,##0) |
|24 |\"$\"#,##0.00;(\"$\"#,##0.00) |
|25 |\"$\"#,##0.00;(\"$\"#,##0.00) |
|26 |\"$\"#,##0.00_);(\"$\"#,##0.00) |
|27 |M月D日|
|28 |M月D日|
|29 |M月D日|
|30 |M/D/YY |
|31 |YYYY年M月D日|
|32 |h 时 mm 分 |
|33 |h\ 时 \"mm\" 分 \"ss\" 秒 \" |
|34 |tth 时 mm 分 |
|35 |tth 时 mm 分 ss 秒 |
|36 |YYYY年M月|
|37 |_(#,##0 );(#,##0) |
|38 |_(#,##0 );(#,##0) |
|39 |_(#,##0.00 );(#,##0.00) |
|40 |_(#,##0.00 );(#,##0.00) |
|41 |*(\"$\"* ***#,##0** **);*** **(\"$\"** *_(#,##0);* (\"$\"*\"-\" *);* (@_) |
|42 |*(* ***#,##0** **);*** **(** *_(#,##0);* (*-\" *);* (@_) |
|43 |*(* ***#,##0.00** **);*** **(** *_(#,##0.00);* (*-\"?? *);* (@_) |
|44 |*(\"$\"* ***#,##0.00** **);*** **(\"$\"** *_(#,##0.00);* (\"$\"*\"-\"?? *);* (@_) |
|45 |mm:ss |
|46 |h:mm:ss |
|47 |mm:ss.0 |
|48 |##0.0E+0 |
|49 |@ |
|50 |YYYY年M月|
|51 |M月D日|
|52 |YYYY年M月|
|53 |M月D日|
|54 |M月D日|
|55 |tth 时 mm 分 |
|56 |tth 时 mm 分 ss 秒 |
|57 |YYYY年M月|
|58 |M月D日|

{{% alert color="primary" %}} 

I några nummerformat kan du märka vissa tecken som 月. Detta är egentligen kinesiska tecken och kan användas i kinesiska och japanska versioner av MS Excel.

{{% /alert %}} 

### **Nummerformat som stöds i Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb stödjer också 59 typer av nummerformat som listas nedan:

|**Nummerformatstyper**|**Nummerformat**|
| :- | :- |
|General |General |
|Decimal1 |0 |
|Decimal2 |0.00 |
|Decimal3 |#,##0 |
|Decimal4 |#,##0.00 |
|Currency1 |$#,##0;$-#,##0 |
|Currency2 |$#,##0;$-#,##0 |
|Currency3 |$#,##0.00;$-#,##0.00 |
|Currency4 |$#,##0.00;$-#,##0.00 |
|Currency5 |#,##0;-#,##0 |
|Currency6 |#,##0;-#,##0 |
|Currency7 |#,##0.00;-#,##0.00 |
|Currency8 |#,##0.00;-#,##0.00 |
|Currency9 |$#,##0;($#,##0) |
|Currency10 |$#,##0;($#,##0) |
|Currency11 |$#,##0.00;($#,##0.00) |
|Currency12 |$#,##0.00;($#,##0.00) |
|Percentage1 |0% |
|Percentage2 |0.00% |
|Scientific1 |0.00E+00 |
|Scientific2 |##0.0E+00 |
|Fraction1 |#?/? |
|Fraction2 |# */*|
|Date1 |m/d/yy |
|Date2 |d-mmm-yy |
|Date3 |d-mmm |
|Date4 |mmm-yy |
|Time1 |h:mm AM/PM |
|Time2 |h:mm:ss AM/PM |
|Time3 |h:mm |
|Time4 |h:mm:ss |
|Time5 |m/d/yy h:mm |
|Time6 |mm:ss |
|Time7 |h: mm:ss |
|Time8 |mm:ss.0 |
|Accounting1 |_ * #,##0_ ;_ * "_ ;_ @_ |
|Accounting2 |_ $* #,##0_ ;_ $* "_ ;_ @_ |
|Accounting3 |_ * #,##0.00_ ;_ * "??_ ;_ @_ |
|Accounting4 |_ $* #,##0.00_ ;_ $* "??_ ;_ @_ |
|Text |@ |
|EasternDate1 |YYYY?M? |
|EasternDate2 |M?D? |
|EasternDate3 |M?D? |
|EasternDate4 |M/D/YY |
|EasternDate5 |YYYY?M?D? |
|EasternDate6 |YYYY?M? |
|EasternDate7 |YYYY?M? |
|EasternDate8 |M?D? |
|EasternDate9 |YYYY?M? |
|EasternDate10 |M?D? |
|EasternDate11 |M?D? |
|EasternDate12 |YYYY?M? |
|EasternDate13 |M?D? |
|EasternTime1 |h?mm? |
|EasternTime2 |h?mm?ss? |
|EasternTime3 |tth?mm? |
|EasternTime4 |tth?mm?ss |
|EasternTime5 |tth?mm? |
|EasternTime6 |tth?mm?ss |
