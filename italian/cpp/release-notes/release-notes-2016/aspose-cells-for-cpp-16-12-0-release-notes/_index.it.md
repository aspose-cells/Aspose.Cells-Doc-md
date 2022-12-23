---
title: Aspose.Cells per le note di rilascio di CPP 16.12.0
type: docs
weight: 10
url: /it/cpp/aspose-cells-for-cpp-16-12-0-release-notes/
---
|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSPORTINGC-432|Applicare la formattazione condizionale alle celle|Nuova caratteristica|
|CELLSPORTINGC-433|Lettura/scrittura di proprietà documento personalizzate|Nuova caratteristica|
|CELLSPORTINGC-434|Lettura/scrittura Proprietà del documento integrate|Nuova caratteristica|
|CELLSPORTINGC-435|Aggiungi collegamenti ipertestuali alle celle|Nuova caratteristica|
|CELLSPORTINGC-436|Supporta i temi di MS Excel|Nuova caratteristica|
|CELLSPORTINGC-437|Aggiungere e manipolare le tabelle pivot nel foglio di calcolo|Nuova caratteristica|
|CELLSPORTINGC-438|Raggruppa righe e colonne nel foglio di lavoro|Nuova caratteristica|
|CELLSPORTINGC-439|Aggiungi oggetto tabella/elenco al foglio di lavoro|Nuova caratteristica|
|CELLSPORTINGC-426|Problema di licenza con le API Aspose.Cells for C++|Insetto|
|CELLSPORTINGC-425|Ottimizza le prestazioni del salvataggio dei file XLS|Miglioramento|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for C++. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Rinomina il metodo ICell::SetStyle in ICell::SetIStyle**
#### **Rinomina il metodo ICell::SetCharacters in ICell::SetIFontSettings**
#### **Rinomina il metodo ICellsColor::SetThemeColor in ICellsColor::SetIThemeColor**
#### **Rinomina il metodo ICells::SetStyle in ICells::SetIStyle**
#### **Rinomina il metodo ICellsHelper::GetDPI_i in ICellsHelper::GetDPI**
#### **Rinomina il metodo ICellsHelper::SetDPI_i in ICellsHelper::SetDPI**
#### **Rinomina il metodo ICellsHelper::GetVersion_i in ICellsHelper::GetVersion**
#### **Rinomina il metodo ICellsHelper::IsProtectedByRMS_i in ICellsHelper::IsProtectedByRMS**
#### **Rinomina il metodo ICellsHelper::IsProtectedByRMS_i in ICellsHelper::IsProtectedByRMS**
#### **Rinomina il metodo ICellsHelper::CellNameToIndex_i in ICellsHelper::CellNameToIndex**
#### **Rinomina il metodo ICellsHelper::CellIndexToName_i in ICellsHelper::CellIndexToName**
#### **Rinomina il metodo ICellsHelper::ColumnIndexToName_i in ICellsHelper::ColumnIndexToName**
#### **Rinomina il metodo ICellsHelper::ColumnNameToIndex_i in ICellsHelper::ColumnNameToIndex**
#### **Rinomina il metodo ICellsHelper::RowIndexToName_i in ICellsHelper::RowIndexToName**
#### **Rinomina il metodo ICellsHelper::RowNameToIndex_i in ICellsHelper::RowNameToIndex**
#### **Rinomina il metodo ICellsHelper::ConvertR1C1FormulaToA1_i in ICellsHelper::ConvertR1C1FormulaToA1**
#### **Rinomina il metodo ICellsHelper::ConvertA1FormulaToR1C1_i in ICellsHelper::ConvertA1FormulaToR1C1**
#### **Rinomina il metodo ICellsHelper::GetDateTimeFromDouble_i in ICellsHelper::GetDateTimeFromDouble**
#### **Rinomina il metodo ICellsHelper::GetDoubleFromDateTime_i in ICellsHelper::GetDoubleFromDateTime**
#### **Rinomina il metodo ICellsHelper::DetectLoadFormat_i in ICellsHelper::DetectLoadFormat**
#### **Rinomina il metodo ICellsHelper::DetectFileFormat_i in ICellsHelper::DetectFileFormat**
#### **Rinomina il metodo ICellsHelper::GetFontDir_i in ICellsHelper::GetFontDir**
#### **Rinomina il metodo ICellsHelper::SetFontDir_i in ICellsHelper::SetFontDir**
#### **Rinomina il metodo ICellsHelper::GetFontDirs_i in ICellsHelper::GetFontDirs**
#### **Rinomina il metodo ICellsHelper::SetFontDirs_i in ICellsHelper::SetFontDirs**
#### **Rinomina il metodo ICellsHelper::GetFontFiles_i in ICellsHelper::GetFontFiles**
#### **Rinomina il metodo ICellsHelper::SetFontFiles_i in ICellsHelper::SetFontFiles**
#### **Rinomina il metodo ICellsHelper::GetStartupPath_i in ICellsHelper::GetStartupPath**
#### **Rinomina il metodo ICellsHelper::SetStartupPath_i in ICellsHelper::SetStartupPath**
#### **Rinomina il metodo ICellsHelper::GetAltStartPath_i in ICellsHelper::GetAltStartPath**
#### **Rinomina il metodo ICellsHelper::SetAltStartPath_i in ICellsHelper::SetAltStartPath**
#### **Rinomina il metodo ICellsHelper::GetLibraryPath_i in ICellsHelper::GetLibraryPath**
#### **Rinomina il metodo ICellsHelper::SetLibraryPath_i in ICellsHelper::SetLibraryPath**
#### **Rinomina il metodo ICellsHelper::GetUsedColors_i in ICellsHelper::GetUsedColors**
#### **Rinomina il metodo ICellsHelper::AddAddInFunction_i in ICellsHelper::AddAddInFunction**
#### **Rinomina il metodo ICellsHelper::MergeFiles_i in ICellsHelper::MergeFiles**
#### **Rinomina il metodo IColumnCollection::GetByIndex_i in IColumnCollection::GetIColumn**
#### **Rinomina il metodo IFileFormatUtil::DetectFileFormat_i in IFileFormatUtil::DetectFileFormat**
#### **Rinomina il metodo IFileFormatUtil::ExtensionToSaveFormat_i in IFileFormatUtil::ExtensionToSaveFormat**
#### **Rinomina il metodo IFileFormatUtil::IsTemplateFormat_i in IFileFormatUtil::IsTemplateFormat**
#### **Rinomina il metodo IFileFormatUtil::LoadFormatToExtension_i in IFileFormatUtil::LoadFormatToExtension**
#### **Rinomina il metodo IFileFormatUtil::LoadFormatToSaveFormat_i in IFileFormatUtil::LoadFormatToSaveFormat**
#### **Rinomina il metodo IFileFormatUtil::SaveFormatToExtension_i in IFileFormatUtil::SaveFormatToExtension**
#### **Rinomina il metodo IFileFormatUtil::SaveFormatToLoadFormat_i in IFileFormatUtil::SaveFormatToLoadFormat**
#### **Rinomina il metodo IRange::SetStyle in IRange::SetIStyle**
#### **Rinomina il metodo IFindOptions::SetRange in IFindOptions::SetIRange**
#### **Rinomina il metodo ILoadOptions::SetLoadDataOptions in ILoadOptions::SetILoadDataOptions**
#### **Rinomina il metodo IWorkbook::SetSettings in IWorkbook::SetISettings**
#### **Rinomina il metodo IWorkbook::SetDefaultStyle in SetDefaultIStyle**
