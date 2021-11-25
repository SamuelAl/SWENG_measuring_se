import { React, Component } from 'react'
import axios from "axios"
import { Disclosure } from '@headlessui/react'
import { SearchIcon } from '@heroicons/react/solid'
import { BellIcon, MenuIcon, XIcon } from '@heroicons/react/outline'
import DataChart from './DataChart'
import TextInput from './TextInput'
import UserBadge from './UserBadge'
import Toggle from './Toggle'

const navigation = [
    { name: 'Dashboard', href: '#', current: true },
    { name: 'About', href: '#', current: false },
]

function classNames(...classes) {
    return classes.filter(Boolean).join(' ')
}

export default class Dashboard extends Component {

    state = {
        repo: "",
        contributor: null,
        data: [],
        contributors: [],
        normalize: false
    }

    componentDidMount() {
    }

    fetchData = () => {
        this.fetchCommitStats()
        this.fetchContributors()
    }

    fetchCommitStats = () => {
        const {repo, contributor, normalize} =  this.state
        let params = {
            repo: repo,
            normalize: normalize
        }
        if (contributor && contributor !== "") {
            params.user = contributor
        }
        axios.get('http://10.5.64.223:105/api/repo', {
            params: params
        })
            .then(res => {
                console.log(res.data)
                let prcData = this.processData(res.data)
                this.setState({
                    data: prcData
                })
            })
    }

    fetchContributors = () => {
        axios.get('http://10.5.64.223:105/api/repo/contributors', {
            params: {
                repo: this.state.repo
            }
        })
            .then(res => {
                let contributors = res.data
                console.log(res.data)
                this.setState({
                    contributors: contributors
                })
            })
    }

    handleChange = (e) => {
        this.setState({
            [e.target.id]: e.target.value
        })
    }

    handleToggleNormalize = (v) => {
        this.setState({
            normalize: v
        }, this.fetchCommitStats)
    }

    handleSelectContributor = (c) => {
        this.setState({
            contributor: c
        }, () => this.fetchCommitStats())
    }

    handleSearch = () => {
        this.setState({
            contributor: null
        }, () => {
            this.fetchData()
        })
    }

    processData = (rawData) => {
        return rawData
            .map((value) => {
                return ({
                    date: value.date,
                    additions: value.stats.additions,
                    changes: value.stats.changes,
                    deletions: value.stats.deletions,
                })
            })
            .sort((a, b) => a.date.localeCompare(b.date))
    }

    render() {
        return (
            <>
                <div className="min-h-full">
                    <div className="bg-indigo-600 pb-32">
                        <nav className="bg-indigo-600 border-b border-indigo-300 border-opacity-25 lg:border-none">
                            <>
                                <div className="max-w-7xl mx-auto px-2 sm:px-4 lg:px-8">
                                    <div className="relative h-16 flex items-center justify-between lg:border-b lg:border-indigo-400 lg:border-opacity-25">
                                        <div className="px-2 flex items-center lg:px-0">
                                            <div className="flex-shrink-0">
                                                <img
                                                    className="block h-8 w-8"
                                                    src="https://tailwindui.com/img/logos/workflow-mark-indigo-300.svg"
                                                    alt="Workflow"
                                                />
                                            </div>
                                            <div className="hidden lg:block lg:ml-10">
                                                <div className="flex space-x-4">
                                                    {navigation.map((item) => (
                                                        <a
                                                            key={item.name}
                                                            href={item.href}
                                                            className={classNames(
                                                                item.current
                                                                    ? 'bg-indigo-700 text-white'
                                                                    : 'text-white hover:bg-indigo-500 hover:bg-opacity-75',
                                                                'rounded-md py-2 px-3 text-sm font-medium'
                                                            )}
                                                            aria-current={item.current ? 'page' : undefined}
                                                        >
                                                            {item.name}
                                                        </a>
                                                    ))}
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </>
                        </nav>
                        <header className="py-10">
                            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                                <h1 className="text-3xl font-bold text-white">
                                    Refactoring Visualization
                                </h1>
                                <h3 className="text-xl font-semibold text-white">
                                    Visualize the proportion of additions and deletions in a repo's history,
                                    from its creation to its present state.
                                </h3>
                            </div>
                        </header>
                    </div>

                    <main className="h-full -mt-32">
                        <div className="max-w-7xl mx-auto pb-12 px-4 sm:px-6 lg:px-8">
                            <div className="flex flex-col bg-white rounded-lg shadow my-6 px-5 py-6 sm:px-6">
                                <div className="mb-4">
                                    <h3 className="text-xl font-semibold text-black">
                                        Repository Details
                                    </h3>
                                </div>
                                <div className="flex gap-2 items-end">
                                    <div className="w-60">
                                        <TextInput params={
                                            {
                                                type: "text",
                                                label: "Repository Name",
                                                id: "repo",
                                                name: "repo_name",
                                                placeholder: "SamuelAl/hexbin",
                                                onChange: this.handleChange,
                                                value: this.state.repo
                                            }
                                        } />
                                    </div>
                                    <button
                                        type="button"
                                        className="inline-flex h-10 items-center px-4 py-2 border border-transparent shadow-sm text-base font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                                        onClick={this.handleSearch}
                                    >
                                        <SearchIcon className="-ml-1 mr-3 h-5 w-5" aria-hidden="true" />
                                        Search
                                    </button>
                                    
                                    <div className="ml-10">
                                    <Toggle label="Normalize Data" enabled={this.state.normalize} onChange={this.handleToggleNormalize} />
                                    </div>
                                    
                                    
                                    
                                </div>
                            </div>

                            <div className="grid grid-cols-4 gap-8">
                                <div className="col-span-3 flex justify-center bg-white rounded-lg shadow px-5 py-6 sm:px-6">
                                    {this.state.data != null &&
                                        <DataChart data={this.state.data}></DataChart>
                                    }
                                </div>
                                <div className="col-span-1 flex-col gap-2 bg-white px-5 py-6 sm:px-6 overflow-auto"
                                    style={{height: "600px"}}>
                                    <div className="mb-4">
                                        <h3 className="text-xl font-semibold">Selected User:</h3>
                                        <p className="text-lg">{this.state.contributor ? this.state.contributor : "All"}</p>
                                    </div>
                                    {this.state.contributors && this.state.contributors.map((c) => <UserBadge user={c} 
                                               onClick={this.handleSelectContributor} />)}
                                </div>
                            </div>
                        </div>
                    </main>
                </div>
            </>
        )
    }
}