---
title : "Public API Changes in Aspose.Cells 8.2.0" 
description : "" 
weight : 12293 
toc : false
type: docs
url: /java/developerguide/migratingfromearliervs/public+api+changes+in+aspose.cells+8.2.0/
---

# Aspose.Cells for Java : Public API Changes in Aspose.Cells 8.2.0


This document describes changes to the Aspose.Cells API from version 8.1.2 to 8.2.0, that may be of interest to module/application developers. It includes not only new and updated public methods, but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

### Added MultiThreadReading Property for Cells Class

With Aspose.Cells for Java 8.2.0, the `MultiThreadReading` property has been added to the `Cells` class in order to provide more robust mechanism to read cells values with multiple threads simultaneously. Setting the Boolean type property to true in the multi-threaded application makes sure that each thread will receive the correct cells value.

Please check the detailed article on [Simultaneously Read Cells Values in Multi-Threaded Environment](http://www.aspose.com/docs/display/cellsjava/Reading+Cell+Values+in+Multiple+Threads+Simultaneously) for more information.

### Added Overloads for autoFitRows & autoFitColumns Methods

New overloads for `autoFitRows` & `autoFitColumns` have been added to the `Worksheet` class, allowing the developers to auto fit the rows & columns based on their respective ranges while passing an instance of the `AutoFitterOptions` class.

The signatures of aforesaid methods are as follow:

1.  autoFitRows(int startRow, int endRow, AutoFitterOptions options)
2.  autoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions options)

Please check the detailed article on [Auto Fit Rows and Columns](http://aspose.com/docs/display/cellsjava/AutoFit+Rows+and+Columns).

