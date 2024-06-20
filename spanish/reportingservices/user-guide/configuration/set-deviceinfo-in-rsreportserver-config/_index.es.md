---
title: Establecer DeviceInfo en rsreportserver.config
type: docs
weight: 60
url: /es/reportingservices/set-deviceinfo-in-rsreportserver-config/
---

- **FileExtension** 
  Cuando el valor es nulo, el nombre de extensión del archivo de informe exportado será el valor predeterminado. Cuando el valor no es nulo, el nombre de extensión del archivo de informe exportado es el valor.
- **SimplePageHeaders** 
  Cuando el valor es verdadero, renderiza el elemento de encabezado de informe en el encabezado de página Excel. El valor predeterminado es falso.
- **SimplePageFooters** 
  Cuando el valor es verdadero, renderiza el elemento de pie de informe en el pie de página Excel. El valor predeterminado es true.
- **PutoutHeader** 
  Cuando el valor es verdadero, exportará el elemento de encabezado de informe. Cuando el valor es falso, no exportará el elemento de encabezado de informe. El valor predeterminado es true. El valor solo admite la extensión Excel2007Xlsx (Solo datos).
- **PutoutFooter** 
  Cuando el valor es verdadero, exportará el elemento de pie de informe. Cuando el valor es falso, no exportará el elemento de pie de informe. El valor predeterminado es true. El valor solo admite la extensión Excel2007Xlsx (Solo datos).
- **FillTableGroupHeaderForSimpleOutPut** 
  El valor predeterminado es falso. El valor solo admite la extensión Excel2007Xlsx (Solo datos).
- **NoOutPutTotalForSimpleOutPut** 
  El valor predeterminado es falso. El valor solo admite la extensión Excel2007Xlsx (Solo datos).
- **NoOutPutGroupForSimpleOutPut** 
  El valor predeterminado es falso. El valor solo admite la extensión Excel2007Xlsx (Solo datos).
- **NoDoGroupPageForSimpleOutPut** 
  El valor predeterminado es true. El valor solo admite la extensión Excel2007Xlsx (solo datos).
- **NoDoPageForSimpleOutPut** 
  El valor predeterminado es true. El valor solo admite la extensión Excel2007Xlsx (solo datos).
- **FieldDelimiter** 
  Establece los delimitadores de campo. El valor admite las extensiones CSV y TXT. 
