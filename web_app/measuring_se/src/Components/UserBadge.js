import React from 'react'

export default function UserBadge({ user }) {
    return (
        <div className="flex  gap-3  bg-white rounded-md shadow hover:shadow-lg w-full h-20 overflow-hidden">
            <img src={user.avatar_url} alt="" />
            <div className="mt-4">
                <span className="text-lg text-gray-700">
                    {user.login}
                </span>
            </div>

        </div>
    )
}
