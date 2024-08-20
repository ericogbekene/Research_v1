const Sidebar = () => {
    return (
      <>
        {/** Insert search bar */}
        <div className="w-70 h-full bg-gray-800 text-white p-4">
          <div className="mb-4">
            <input
              type="text"
              placeholder="Search..."
              className="w-full px-2 py-1 rounded-md bg-gray-700 text-white focus:outline-none focus:ring focus:ring-gray-500"
            />
          </div>
          <div className="mb-4">
            <h2 className="text-lg font-semibold">Departments</h2>
          </div>
          <div>
            <h2 className="text-lg font-semibold">Settings</h2>
          </div>
        </div>
      </>
    );
  };

  export default Sidebar;
