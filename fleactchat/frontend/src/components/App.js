import React from 'react';
import DataProvider from "./DataProvider";
import Table from "./Table";

const App = () => (
    <DataProvider endpoint="api/lead/"
                  render={data => <Table data={data}/>}/>
);

export default App