import { useState, useEffect } from 'react'
import M from 'materialize-css'
import './App.css'

function App() {
  const [activeTab, setActiveTab] = useState('dashboard')
  const [searchTerm, setSearchTerm] = useState('')
  const [searchByTag, setSearchByTag] = useState('')
  const [documents, setDocuments] = useState([
    { 
      id: 1, 
      name: 'Employee Records.pdf', 
      status: 'processed', 
      piiCount: 15, 
      lastScanned: '2024-03-20',
      tags: ['hr', 'confidential', 'employee']
    },
    { 
      id: 2, 
      name: 'Customer Data.xlsx', 
      status: 'pending', 
      piiCount: 0, 
      lastScanned: null,
      tags: ['customers', 'sales']
    },
    { 
      id: 3, 
      name: 'Medical Records.doc', 
      status: 'flagged', 
      piiCount: 47, 
      lastScanned: '2024-03-19',
      tags: ['medical', 'confidential']
    }
  ])

  const [activities] = useState([
    { id: 1, type: 'upload', user: 'Admin', file: 'Financial Report.pdf', timestamp: '2024-03-21 14:30' },
    { id: 2, type: 'redact', user: 'John', file: 'Customer Data.xlsx', timestamp: '2024-03-21 13:15' },
    { id: 3, type: 'share', user: 'Sarah', file: 'Employee Records.pdf', timestamp: '2024-03-21 11:45' },
    { id: 4, type: 'download', user: 'Mike', file: 'Medical Records.doc', timestamp: '2024-03-21 10:20' }
  ])

  const [showUploadModal, setShowUploadModal] = useState(false)

  const [stats] = useState({
    totalDocuments: documents.length,
    documentsWithPII: documents.filter(doc => doc.piiCount > 0).length,
    totalPIIFound: documents.reduce((total, doc) => total + doc.piiCount, 0),
    recentAlerts: documents.filter(doc => doc.status === 'flagged').length
  })

  useEffect(() => {
    // Initialize sidenav
    const elems = document.querySelectorAll('.sidenav')
    M.Sidenav.init(elems, { edge: 'left' })
  }, [])

  const filteredDocuments = documents.filter(doc => {
    const nameMatch = doc.name.toLowerCase().includes(searchTerm.toLowerCase())
    const tagMatch = doc.tags.some(tag => 
      tag.toLowerCase().includes(searchByTag.toLowerCase())
    )
    return searchTerm ? nameMatch : searchByTag ? tagMatch : true
  })

  const renderDashboard = () => (
    <div className="dashboard-content animate__animated animate__fadeIn">
      {/* Stats Section */}
      <div className="row">
        <div className="col s12 m6 l3">
          <div className="card-panel teal white-text">
            <i className="material-icons medium">description</i>
            <h5>Total Documents</h5>
            <h3>{stats.totalDocuments}</h3>
          </div>
        </div>
        <div className="col s12 m6 l3">
          <div className="card-panel blue white-text">
            <i className="material-icons medium">warning</i>
            <h5>Documents with PII</h5>
            <h3>{stats.documentsWithPII}</h3>
          </div>
        </div>
        <div className="col s12 m6 l3">
          <div className="card-panel orange white-text">
            <i className="material-icons medium">privacy_tip</i>
            <h5>Total PII Found</h5>
            <h3>{stats.totalPIIFound}</h3>
          </div>
        </div>
        <div className="col s12 m6 l3">
          <div className="card-panel red white-text">
            <i className="material-icons medium">notifications</i>
            <h5>Recent Alerts</h5>
            <h3>{stats.recentAlerts}</h3>
          </div>
        </div>
      </div>

      {/* Recent Activities Section */}
      <div className="row">
        <div className="col s12 m6">
          <div className="card">
            <div className="card-content">
              <span className="card-title">Recent Activities</span>
              <ul className="activity-list">
                {activities.map(activity => (
                  <li key={activity.id} className="activity-item">
                    <i className="material-icons activity-icon">
                      {activity.type === 'upload' ? 'upload_file' :
                       activity.type === 'redact' ? 'security' :
                       activity.type === 'share' ? 'share' : 'download'}
                    </i>
                    <div className="activity-details">
                      <p><strong>{activity.user}</strong> {activity.type}ed <span className="file-name">{activity.file}</span></p>
                      <span className="activity-time">{activity.timestamp}</span>
                    </div>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>

        {/* Documents Section */}
        <div className="col s12 m6">
          <div className="card">
            <div className="card-content">
              <span className="card-title">Document Management</span>
              <button className="btn waves-effect waves-light" onClick={() => setShowUploadModal(true)}>
                <i className="material-icons left">cloud_upload</i>
                Upload New Document
              </button>
              
              <div className="documents-list">
                {filteredDocuments.map(doc => (
                  <div key={doc.id} className="document-item">
                    <div className="document-info">
                      <i className="material-icons document-type">
                        {doc.name.endsWith('.pdf') ? 'picture_as_pdf' :
                         doc.name.endsWith('.xlsx') ? 'table_chart' : 'description'}
                      </i>
                      <span className="document-name">{doc.name}</span>
                      <span className={`status-badge ${doc.status}`}>{doc.status}</span>
                    </div>
                    <div className="document-actions">
                      <button className="btn-small" title="View">
                        <i className="material-icons">visibility</i>
                      </button>
                      <button className="btn-small blue" title="Redact PII">
                        <i className="material-icons">security</i>
                      </button>
                      <button className="btn-small green" title="Share">
                        <i className="material-icons">share</i>
                      </button>
                      <button className="btn-small orange" title="Download">
                        <i className="material-icons">download</i>
                      </button>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )

  return (
    <div className="admin-dashboard">
      {/* Sidebar Navigation */}
      <ul id="slide-out" className="sidenav sidenav-fixed">
        <li>
          <div className="user-view">
            <div className="background blue darken-2">
              <div className="pattern-overlay"></div>
            </div>
            <a href="#"><i className="material-icons large white-text">security</i></a>
            <a href="#"><span className="white-text name">DataRakshak Admin</span></a>
          </div>
        </li>
        
        <li className="search-box">
          <div className="input-field">
            <i className="material-icons prefix">search</i>
            <input 
              type="text" 
              placeholder="Search files..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
            />
          </div>
        </li>
        
        <li className="search-box">
          <div className="input-field">
            <i className="material-icons prefix">local_offer</i>
            <input 
              type="text" 
              placeholder="Search by tag..."
              value={searchByTag}
              onChange={(e) => setSearchByTag(e.target.value)}
            />
          </div>
        </li>

        <li><div className="divider"></div></li>
        
        <li>
          <a 
            className={activeTab === 'dashboard' ? 'active' : ''} 
            onClick={() => setActiveTab('dashboard')}
          >
            <i className="material-icons">dashboard</i>Dashboard
          </a>
        </li>
        <li>
          <a 
            className={activeTab === 'scanner' ? 'active' : ''} 
            onClick={() => setActiveTab('scanner')}
          >
            <i className="material-icons">search</i>PII Scanner
          </a>
        </li>
        <li>
          <a 
            className={activeTab === 'settings' ? 'active' : ''} 
            onClick={() => setActiveTab('settings')}
          >
            <i className="material-icons">settings</i>Settings
          </a>
        </li>
      </ul>

      {/* Main Content */}
      <div className="main-content">
        <nav className="top-nav">
          <div className="nav-wrapper">
            <a href="#" data-target="slide-out" className="sidenav-trigger">
              <i className="material-icons">menu</i>
            </a>
            <div className="nav-title">{activeTab.charAt(0).toUpperCase() + activeTab.slice(1)}</div>
          </div>
        </nav>

        <div className="container">
          {activeTab === 'dashboard' && renderDashboard()}
          {activeTab === 'scanner' && <div>Scanner Content</div>}
          {activeTab === 'settings' && <div>Settings Content</div>}
        </div>
      </div>
    </div>
  )
}

export default App
