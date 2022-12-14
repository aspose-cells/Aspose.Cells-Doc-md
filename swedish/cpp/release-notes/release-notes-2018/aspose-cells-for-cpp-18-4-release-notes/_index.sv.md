---
title: Aspose.Cells för CPP 18.4 Release Notes
type: docs
weight: 30
url: /sv/cpp/aspose-cells-for-cpp-18-4-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells för CPP 18.4.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSCPP-53|Stöd ritningsfunktioner/moduler|Ny funktion|
|CELLSCPP-57|Implementera System.Drawing bibliotek|Ny funktion|
|CELLSCPP-68|Debug System.Drawing modul|Ny funktion|
|CELLSCPP-69|Lös problem i C++ testfall|Ny funktion|
|CELLSCPP-70|Lös minnesläckage i klasser av System.Drawing-moduler|Ny funktion|
|CELLSCPP-73|Skriv en metod för att publicera .h-filer|Ny funktion|
|CELLSCPP-75|Implementera C++-funktionen: Rita bild från Stream|Ny funktion|
|CELLSCPP-76|Implementera C++-klasser: ComIStreamWrapper, Metafile|Ny funktion|
|CELLSCPP-77|Debug C++ testfall: Kopior|Ny funktion|
|CELLSCPP-78|Lös problem i C++-testfall: DigitalSignature, EnumTypes, Fynd, Formler, Hyperlinks-moduler|Ny funktion|
|CELLSCPP-79|Lös länkproblemet för C++-versionen|Ny funktion|
|CELLSCPP-81|Fixa FillPath-problemet i grafikmodulen|Ny funktion|
|CELLSCPP-82|Fixa System.Drawing-modulproblem efter testfall|Ny funktion|
|CELLSCPP-83|Fixa gppoint FillPath-problem i grafikmodulen|Ny funktion|
|CELLSCPP-89|Översätt och felsök testfall i katalogen Charts/EnumTypes|Ny funktion|
|CELLSCPP-91|Översätt testfall i Finds|Ny funktion|
|CELLSCPP-96|Översätt och felsök testfall i katalogen Formler/Hyperlänkar/ImpHtml/ImportExports/Inserts|Ny funktion|
|CELLSCPP-97|Felsök och fixa problem angående XLSX/XLS till PDF-rendering|Ny funktion|
|CELLSCPP-98|Översätt och felsök testfall i LightCells katalog|Ny funktion|
|CELLSCPP-100|Översätt och felsök testfall i katalogen Merges/OpenSaves/PageSetups/PDF|Ny funktion|
|CELLSCPP-101|Översätt och felsök testfall i PivotTables-katalogen|Ny funktion|
|CELLSCPP-102|Diagram analyseras (behålls) inte när ett XLSX-filformat öppnas/sparas|Ny funktion|
|CELLSCPP-103|Översätt och felsök testfall i Shapes-katalogen|Ny funktion|
|CELLSCPP-105|Översätt och felsök testfall i XlsxTest-katalogen|Ny funktion|
|CELLSCPP-108|Öppna filer och kontrollera diagramrelaterade problem|Ny funktion|
|CELLSCPP-106|Problem med minnesläckage|Insekt|
### **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, omdöpta, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells för C++. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
#### **Byter namn på alla metoder som 'SetIs*' till 'Set*'-metoder**
Byter namn på metoder, såsom SetIsOutlineShown till SetIsOutlineShown, SetIsSelected till SetSelected i IWorksheet och så vidare. För mer information, se API-referensguide.
#### **Ändrar färg till System::Drawing::Color**
Till exempel ändrar den Color::GetBlue() till System::Drawing::Color::GetBlue(). Eftersom färg är en tvetydig symbol här kan det vara Aspose::Cells::System::Drawing::Color eller Gdiplus::Color. För att använda Färg i Aspose Cells måste du lägga till namnutrymme System::Drawing.
#### **Byter namn på ICells::AddRange till AddIRange**
Lägger till en intervallobjektreferens till celler.
#### **Byter namn på ICells::ApplyColumnStyle till ApplyColumnIStyle**
Tillämpar formatering för en hel kolumn.
#### **Byter namn på ICells::ApplyRowStyle till ApplyRowIStyle**
Tillämpar formatering för en hel rad.
#### **Byter namn på ICells::ApplyStyle till ApplyIStyle**
Tillämpar formatering för ett helt kalkylblad.
#### **Byter namn på ICells::CopyColumn till CopyIColumn**
Kopierar data och formatering av en hel kolumn.
#### **Byter namn på ICells::CopyColumns till CopyIColumns**
Kopierar data och formatering av specificerade kolumner.
#### **Byter namn på ICells::CopyColumns till CopyIColumns**
Kopierar data och formatering av specificerade kolumner.
#### **Byter namn på ICells::CopyRow till CopyIRow**
Kopierar data och formatering av en hel rad.
#### **Byter namn på ICells::CopyRows till CopyIRows**
Kopierar data och formatering av specificerade rader.
#### **Byter namn på ICells::MoveRange till MoveIRange**
Flyttar räckvidden till destinationspositionen.
#### **Byter namn på ICells::InsertRange till InsertIRange**
Infogar ett cellintervall och flyttar celler enligt skiftalternativet.
#### **Byter namn på IColumn::ApplyStyle till ApplyIStyle**
Tillämpar formatering för en hel kolumn.
#### **Byter namn på IErrorCheckOption::AddRange till AddIRange**
Lägger till ett påverkat intervall av denna inställning.
#### **Byter namn på IRange::ApplyStyle till ApplyIStyle**
Tillämpar formatering för ett helt intervall.
#### **Byter namn på IRow::ApplyStyle till ApplyIStyle**
Tillämpar formatering för en hel rad.
#### **Byter namn på IPivotField::GetNumberFormat till Get_NumberFormat**
Representerar det anpassade visningsformatet för siffror och datum. Eftersom metodnamnet GetNumberFormat är i konflikt med Windows systemfunktion, så måste vi byta namn på det.
#### **Byter namn på IStyleFlag::GetNumberFormat till Get_NumberFormat**
Eftersom metodnamnet GetNumberFormat är i konflikt med Windows systemfunktion, så måste vi byta namn på det som representerar för att få inställningen Number format.
#### **Byter namn på IWorkbook::CopyTheme till CopyITheme**
Kopierar temat från en annan arbetsbok.
#### **Byter namn på IWorksheet::SetBackground till SetBackgroundImage**
Ställer in kalkylbladets bakgrundsbild.
