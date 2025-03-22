---
title: Queries and Connections with C++
linktitle: Queries and Connections
type: docs
weight: 700
url: /cpp/managing-database-connections/
description: Manage database connections and queries using Aspose.Cells with C++.
---

## **Managing Database Connections**

Aspose.Cells provides robust support for managing database connections and executing queries programmatically. This section explains how to work with database connections and queries in Microsoft Excel files using Aspose.Cells for C++.

### **Establishing a Database Connection**

To establish a database connection, you can use the `Workbook` class, which represents an Excel file. The `Workbook` class contains a `DataConnections` collection that allows you to manage database connections.

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

// Create a new workbook
Workbook workbook;

// Add a new data connection
DataConnection dataConnection = workbook.GetDataConnections().Add("ConnectionName", "ConnectionString");

// Save the workbook
workbook.Save("DatabaseConnections.xlsx");
```

### **Executing Queries**

Once a database connection is established, you can execute queries to retrieve data from the database. The `Worksheet` class provides methods to execute queries and populate the worksheet with the retrieved data.

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

// Load the workbook
Workbook workbook("DatabaseConnections.xlsx");

// Get the first worksheet
Worksheet worksheet = workbook.GetWorksheets().Get(0);

// Execute a query and populate the worksheet
worksheet.GetCells().ImportData("SELECT * FROM TableName", 0, 0);

// Save the workbook
workbook.Save("QueryResults.xlsx");
```

### **Managing Connection Properties**

You can also manage connection properties such as connection string, command text, and refresh settings using the `DataConnection` class.

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

// Load the workbook
Workbook workbook("DatabaseConnections.xlsx");

// Get the first data connection
DataConnection dataConnection = workbook.GetDataConnections().Get(0);

// Set connection properties
dataConnection.SetConnectionString("NewConnectionString");
dataConnection.SetCommandText("SELECT * FROM NewTableName");
dataConnection.SetRefreshOnLoad(true);

// Save the workbook
workbook.Save("UpdatedConnections.xlsx");
```

### **Refreshing Data Connections**

To refresh data connections and update the data in the worksheet, you can use the `RefreshData` method.

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

// Load the workbook
Workbook workbook("DatabaseConnections.xlsx");

// Refresh all data connections
workbook.RefreshAllDataConnections();

// Save the workbook
workbook.Save("RefreshedData.xlsx");
```

### **Handling Connection Errors**

When working with database connections, it's important to handle errors that may occur during the connection or query execution. Aspose.Cells provides mechanisms to handle such errors gracefully.

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

try {
    // Load the workbook
    Workbook workbook("DatabaseConnections.xlsx");

    // Attempt to refresh data connections
    workbook.RefreshAllDataConnections();

    // Save the workbook
    workbook.Save("RefreshedData.xlsx");
} catch (Exception& ex) {
    // Handle the error
    Console::WriteLine("Error: " + ex.GetMessage());
}
```

## **Conclusion**

Aspose.Cells for C++ provides a comprehensive set of features for managing database connections and executing queries in Excel files. By following the examples and guidelines provided in this section, you can effectively work with database connections and queries in your C++ applications.