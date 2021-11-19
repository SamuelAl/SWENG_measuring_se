import {React, Component} from 'react'
import { Disclosure} from '@headlessui/react'
import { SearchIcon } from '@heroicons/react/solid'
import { BellIcon, MenuIcon, XIcon } from '@heroicons/react/outline'
import DataChart from './DataChart'

const navigation = [
    { name: 'Dashboard', href: '#', current: true },
    { name: 'About', href: '#', current: false },
]

function classNames(...classes) {
    return classes.filter(Boolean).join(' ')
}

const data = [
    {
        name: 'Page A',
        uv: 4000,
        pv: 2400,
        amt: 2400,
    },
    {
        name: 'Page B',
        uv: 3000,
        pv: 1398,
        amt: 2210,
    },
    {
        name: 'Page C',
        uv: 2000,
        pv: 9800,
        amt: 2290,
    },
    {
        name: 'Page D',
        uv: 2780,
        pv: 3908,
        amt: 2000,
    },
    {
        name: 'Page E',
        uv: 1890,
        pv: 4800,
        amt: 2181,
    },
    {
        name: 'Page F',
        uv: 2390,
        pv: 3800,
        amt: 2500,
    },
    {
        name: 'Page G',
        uv: 3490,
        pv: 4300,
        amt: 2100,
    },
];
export default class Dashboard extends Component {

    state = {
        data: {}
    }

    componentDidMount() {
        fetch('http://10.5.64.223:105/data/user/SamuelAl/repo/hexbin/')
        .then(response => response.json())
        .then(data => console.log(data))
    }

    render() {
        return (
            <>
                <div className="min-h-full">
                    <div className="bg-indigo-600 pb-32">
                        <Disclosure as="nav" className="bg-indigo-600 border-b border-indigo-300 border-opacity-25 lg:border-none">
                            {({ open }) => (
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
                            )}
                        </Disclosure>
                        <header className="py-10">
                            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                                <h1 className="text-3xl font-bold text-white">Dashboard</h1>
                            </div>
                        </header>
                    </div>
    
                    <main className="h-full -mt-32">
                        <div className="max-w-7xl mx-auto pb-12 px-4 sm:px-6 lg:px-8">
                            {/* Replace with your content */}
                            <div className="flex justify-center  bg-white rounded-lg shadow px-5 py-6 sm:px-6">
                                
                                    <DataChart data={data}></DataChart>
                                
                            </div>
                            {/* /End replace */}
                        </div>
                    </main>
                </div>
            </>
        )
    }
    
}